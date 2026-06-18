import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qr_code(profile):
    """
    Generate QR code for a user profile
    Returns: ContentFile object
    """
    # Your laptop's IP address (from ipconfig)
    YOUR_IP = "10.58.194.93"
    
    # Create the URL - this will work on phone AND laptop
    public_url = f"http://{YOUR_IP}:8000/accounts/public/{profile.uuid}/"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(public_url)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to BytesIO
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    
    # Create ContentFile for Django
    image_content = ContentFile(buffer.getvalue())
    filename = f"qr_{profile.uuid}.png"
    image_content.name = filename
    
    buffer.close()
    
    return image_content