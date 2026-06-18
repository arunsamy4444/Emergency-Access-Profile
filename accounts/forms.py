from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'John Doe'}))
    phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': '+1234567890'}))
    emergency_email_1 = forms.EmailField(required=True, label='Emergency Email', widget=forms.EmailInput(attrs={'placeholder': 'emergency@example.com'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone_number', 'emergency_email_1', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Your Email',
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'emergency_email_1': 'Emergency Contact Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            'password1': 'Your password must contain at least 8 characters.',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Check if profile already exists before creating
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'full_name': self.cleaned_data['full_name'],
                    'phone_number': self.cleaned_data.get('phone_number', ''),
                    'emergency_email_1': self.cleaned_data['emergency_email_1']
                }
            )
            # If profile already exists, update it
            if not created:
                profile.full_name = self.cleaned_data['full_name']
                profile.phone_number = self.cleaned_data.get('phone_number', '')
                profile.emergency_email_1 = self.cleaned_data['emergency_email_1']
                profile.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'phone_number',
            'blood_group',
            'emergency_email_1',
            'emergency_email_2',
            'emergency_contact_1',
            'emergency_contact_2',
            'medical_notes'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+1234567890'}),
            'blood_group': forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px;'}),
            'emergency_email_1': forms.EmailInput(attrs={'placeholder': 'emergency@example.com'}),
            'emergency_email_2': forms.EmailInput(attrs={'placeholder': 'backup@example.com (optional)'}),
            'emergency_contact_1': forms.TextInput(attrs={'placeholder': 'Emergency contact phone 1'}),
            'emergency_contact_2': forms.TextInput(attrs={'placeholder': 'Emergency contact phone 2 (optional)'}),
            'medical_notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Any medical conditions, allergies, or important information'}),
        }
        labels = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'blood_group': 'Blood Group',
            'emergency_email_1': 'Primary Emergency Email',
            'emergency_email_2': 'Secondary Emergency Email',
            'emergency_contact_1': 'Emergency Phone Contact 1',
            'emergency_contact_2': 'Emergency Phone Contact 2',
            'medical_notes': 'Medical Notes',
        }
        help_texts = {
            'emergency_email_1': 'This email will receive emergency alerts when your QR is scanned',
            'emergency_email_2': 'Optional backup contact for emergency alerts',
            'emergency_contact_1': 'Optional - for future SMS notifications',
            'emergency_contact_2': 'Optional - for future SMS notifications',
        }