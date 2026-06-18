# Emergency Access Profile

A web-based emergency identification and contact system that helps connect accident victims, children, elderly individuals, or vulnerable persons with their emergency contacts through QR code scanning.

## Problem

In many emergencies, bystanders are willing to help but often have no way to quickly identify a person or contact their family members.

Examples:

* Road accidents
* Missing children
* Elderly individuals with memory-related conditions
* Medical emergencies
* Individuals unable to communicate

Emergency Access Profile provides a simple solution: scan a QR code and instantly access essential emergency information and contact details.

---

## Features

### User Authentication

* User registration
* Secure login/logout
* Session management

### Emergency Profile Management

Each user can maintain:

* Full Name
* Phone Number
* Blood Group
* Emergency Contact Numbers
* Emergency Contact Emails
* Medical Notes

### QR Code Generation

* Unique QR code for every profile
* Downloadable QR image
* UUID-based public profile access
* Regeneratable QR codes

### Public Emergency Page

Accessible without login.

Displays:

* Name
* Blood Group
* Emergency Contacts
* Medical Notes

Designed for quick access during emergencies.

### Location Sharing

When a QR code is scanned:

* Browser requests location permission
* Latitude and longitude are captured
* Scan event is recorded
* Location can be shared with emergency contacts

### Emergency Alerts

Automatic email notifications include:

* User information
* Scan timestamp
* GPS coordinates
* Google Maps location link
* Medical notes

### Scan Logging

Tracks:

* Scan timestamp
* IP address
* Browser information
* GPS coordinates (when permitted)

---

## System Workflow

1. User creates an account.
2. User completes emergency profile.
3. User generates a QR code.
4. User saves or prints the QR code.
5. QR code is scanned during an emergency.
6. Emergency profile becomes accessible.
7. Scanner optionally shares location.
8. Emergency contacts receive an alert.
9. Scan information is recorded.

---

## Technology Stack

### Backend

* Django

### Database

* Supabase PostgreSQL

### Authentication

* Django Authentication System

### QR Generation

* qrcode
* Pillow

### Notifications

* Gmail SMTP

### Environment Management

* python-dotenv

---

## Project Structure

```text
Emergency-Access-Profile/
├── accounts/
├── core/
├── templates/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/arunsamy4444/Emergency-Access-Profile.git
cd Emergency-Access-Profile
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

SUPABASE_DB_NAME=
SUPABASE_DB_USER=
SUPABASE_DB_PASSWORD=
SUPABASE_DB_HOST=
SUPABASE_DB_PORT=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

---

## Future Improvements

* SMS notifications
* WhatsApp alerts
* Scan history dashboard
* Multi-language support
* Mobile application
* QR sticker printing support
* Emergency contact verification
* Role-based access control
* Encryption of sensitive medical information
* Hospital and public-service integration

---

## Use Cases

### Accident Victims

Emergency contacts can be notified immediately after QR scanning.

### Children

Parents can be contacted if a child is lost.

### Elderly Individuals

Provides identification and emergency contact information.

### Medical Emergencies

Important medical notes become accessible to first responders and bystanders.

---

## Status

Current Status: Prototype

The project currently demonstrates the complete emergency-access workflow from profile creation to QR scanning and emergency contact notification.

---

## Author

Arun Samy

GitHub: https://github.com/arunsamy4444
