import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Optional now
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, blank=True, null=True)
    
    # NEW - Email fields for emergency contacts
    emergency_email_1 = models.EmailField(max_length=254)
    emergency_email_2 = models.EmailField(max_length=254, blank=True, null=True)
    
    emergency_contact_1 = models.CharField(max_length=20, blank=True, null=True)  # Optional now
    emergency_contact_2 = models.CharField(max_length=20, blank=True, null=True)
    medical_notes = models.TextField(blank=True, null=True)
    
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        db_table = 'user_profile'

# NEW - Scan Log Model
class ScanLog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='scans')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    scanned_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.profile.user.username} scanned at {self.scanned_at}"

    class Meta:
        db_table = 'scan_logs'
        ordering = ['-scanned_at']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            full_name=instance.username,
            phone_number='',
            emergency_contact_1='',
            emergency_email_1=''
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(
            user=instance,
            full_name=instance.username,
            phone_number='',
            emergency_contact_1='',
            emergency_email_1=''
        )