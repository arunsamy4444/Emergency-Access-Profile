# Emergency Access Profile

A privacy-focused, open-source emergency access platform designed for children, elderly individuals, and accident victims.

The goal is simple:

**Provide critical emergency information when it is needed, while minimizing unnecessary exposure of personal data.**

---

# Why This Project Exists

In an emergency, bystanders are often willing to help but have no way to identify a person or contact their family.

Existing solutions frequently require users to share large amounts of personal information, maintain persistent records, or rely on centralized systems that retain sensitive data indefinitely.

Emergency Access Profile is being built around a different principle:

> Store only what is necessary. Share only what is necessary. Retain information only as long as it serves a legitimate emergency purpose.

---

# Target Users

## Children

If a child becomes separated from their guardian, a responsible adult can scan the QR code and initiate contact with family members.

## Elderly Individuals

Provides emergency identification and family notification for seniors who may require assistance or have memory-related conditions.

## Accident Victims

Allows first responders or bystanders to access critical emergency information and notify designated contacts.

---

# Current Features

### User Authentication

* User registration
* Secure login and logout
* Session management

### Emergency Profiles

Users can maintain:

* Full Name
* Phone Number
* Blood Group
* Emergency Contact Numbers
* Emergency Contact Emails
* Medical Notes

### QR Code Generation

* Unique QR code for every profile
* Downloadable QR image
* UUID-based public access links

### Public Emergency Access

When a QR code is scanned:

* Emergency profile becomes accessible
* Critical information can be viewed immediately
* Location sharing can be initiated

### Location Sharing

The scanner can voluntarily share their location.

The system captures:

* Latitude
* Longitude
* Timestamp

and can notify designated emergency contacts.

### Emergency Notifications

Automatic email notifications include:

* User information
* Emergency event timestamp
* Shared location
* Google Maps link
* Medical notes

### Scan Logging

For auditing and emergency tracking:

* Scan timestamps
* Location data
* Device information
* IP information

can be recorded during emergency events.

---

# Privacy-First Direction

Emergency Access Profile is being developed with data minimization as a core design goal.

Future versions will focus on reducing unnecessary exposure of personal information while maintaining usability during emergencies.

Planned improvements include:

* OTP-based guardian verification
* Limited public profile visibility
* Temporary emergency event records
* Automatic data expiration policies
* Enhanced privacy controls
* Secure access workflows

The objective is to ensure that strangers can assist during emergencies without gaining unrestricted access to sensitive personal information.

---

# Example Emergency Workflow

1. User creates an emergency profile.
2. User generates a QR code.
3. QR code is attached to belongings, ID cards, or wearable items.
4. A bystander scans the QR code during an emergency.
5. Essential information becomes visible.
6. Scanner may share their location.
7. Emergency contacts receive notifications.
8. Emergency event is logged.
9. Future versions will automatically remove temporary emergency records after a defined retention period.

---

# Technology Stack

### Backend

* Python
* Django

### Database

* PostgreSQL
* Supabase

### Authentication

* Django Authentication Framework

### QR Generation

* qrcode
* Pillow

### Notifications

* SMTP Email Services

### Frontend

* Django Templates

---

# Open Source Mission

Emergency Access Profile is being developed as an open-source project.

The mission is to create emergency communication tools that remain:

* Accessible
* Transparent
* Community-driven
* Privacy-conscious

without relying on invasive tracking, behavioral profiling, or unnecessary data collection.

---

# Project Status

Current Stage: Prototype

Implemented:

* Authentication System
* Emergency Profiles
* QR Code Generation
* Public Emergency Pages
* Location Sharing
* Email Notifications
* Scan Logging

In Development:

* Guardian Verification
* Privacy Controls
* Data Expiration Policies
* Reminder System
* Security Hardening

---
## Prototype Disclaimer

This project is currently an early-stage prototype built to validate the core emergency access workflow.

The current implementation demonstrates:

* User authentication
* Emergency profile management
* QR code generation
* Public emergency access pages
* Location sharing
* Email notifications
* Event logging

However, the system is **not yet production-ready** and should not currently be relied upon as a mission-critical emergency service.

Current limitations include:

* Not designed for large-scale deployment
* Limited security hardening
* No independent security audit
* Basic access-control model
* Limited abuse-prevention mechanisms
* No high-availability infrastructure
* No disaster recovery guarantees
* No formal compliance review

Several important security and privacy features are still under development, including:

* OTP-based guardian verification
* Fine-grained data access controls
* Automatic data expiration policies
* Enhanced encryption strategies
* Advanced audit and monitoring systems
* Privacy-focused access workflows

The purpose of the current prototype is to validate the concept, gather feedback, and guide future development toward a secure, privacy-conscious, and scalable platform.

---

# Long-Term Vision

Build a practical emergency assistance platform that balances two goals:

1. Fast access to critical emergency information.
2. Strong protection of personal data.

The project aims to demonstrate that emergency response tools can remain useful without requiring permanent surveillance or excessive data retention.

---

# Author

Arun Samy

Open Source Project
