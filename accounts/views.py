from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, Http404, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, ProfileForm
from .models import Profile, ScanLog
from .utils import generate_qr_code
import json
import traceback

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html', {
        'username': request.user.username,
        'email': request.user.email,
        'profile': request.user.profile
    })

@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {
        'form': form,
        'profile': profile,
        'user': request.user
    })

@login_required
def generate_qr_view(request):
    profile = request.user.profile
    qr_image = generate_qr_code(profile)
    profile.qr_code.save(f"qr_{profile.uuid}.png", qr_image, save=True)
    messages.success(request, 'QR code generated successfully!')
    return redirect('profile')

@login_required
def download_qr_view(request):
    profile = request.user.profile
    if not profile.qr_code:
        messages.error(request, 'Please generate QR code first.')
        return redirect('profile')
    response = HttpResponse(profile.qr_code.read(), content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="qr_{profile.uuid}.png"'
    return response

def public_profile_view(request, uuid):
    profile = get_object_or_404(Profile, uuid=uuid)
    return render(request, 'public_profile.html', {'profile': profile})

@csrf_exempt
def log_scan_view(request, uuid):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        profile = get_object_or_404(Profile, uuid=uuid)
        data = json.loads(request.body)
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        if not latitude or not longitude:
            return JsonResponse({'error': 'Location data required'}, status=400)
        
        # Save scan log
        scan_log = ScanLog.objects.create(
            profile=profile,
            latitude=latitude,
            longitude=longitude,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )
        
        # Send email alerts (try even if email fails)
        try:
            send_emergency_alerts(profile, latitude, longitude)
        except Exception as e:
            print(f"Email error: {e}")
            # Still return success - location is saved even if email fails
        
        return JsonResponse({'success': True, 'scan_id': scan_log.id})
        
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)

def send_emergency_alerts(profile, latitude, longitude):
    subject = f"🚨 EMERGENCY ALERT: {profile.full_name} needs help!"
    
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    
    message = f"""
    🚨 EMERGENCY CONTACT REQUEST 🚨
    
    {profile.full_name} may need immediate assistance.
    
    ─────────────────────────────
    📋 EMERGENCY INFORMATION:
    ─────────────────────────────
    Full Name: {profile.full_name}
    Blood Group: {profile.blood_group or 'Not specified'}
    Phone: {profile.phone_number or 'Not specified'}
    
    ─────────────────────────────
    📍 SCANNER LOCATION:
    ─────────────────────────────
    Latitude: {latitude}
    Longitude: {longitude}
    Google Maps: {google_maps_link}
    
    ─────────────────────────────
    🏥 MEDICAL NOTES:
    ─────────────────────────────
    {profile.medical_notes or 'No medical notes provided.'}
    
    ─────────────────────────────
    ⏰ SCAN TIME:
    ─────────────────────────────
    {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    ─────────────────────────────
    ℹ️ This is an automated alert from the Emergency Contact System.
    Please contact {profile.full_name} or emergency services if needed.
    """
    
    emails_sent = 0
    
    # Send to primary emergency contact
    if profile.emergency_email_1 and profile.emergency_email_1.strip():
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[profile.emergency_email_1],
                fail_silently=False,
            )
            emails_sent += 1
            print(f"✅ Email sent to {profile.emergency_email_1}")
        except Exception as e:
            print(f"❌ Failed to send to {profile.emergency_email_1}: {e}")
    
    # Send to secondary emergency contact
    if profile.emergency_email_2 and profile.emergency_email_2.strip():
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[profile.emergency_email_2],
                fail_silently=False,
            )
            emails_sent += 1
            print(f"✅ Email sent to {profile.emergency_email_2}")
        except Exception as e:
            print(f"❌ Failed to send to {profile.emergency_email_2}: {e}")
    
    return emails_sent > 0