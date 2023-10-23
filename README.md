# Python Email Client Scripts

These Python scripts allow you to read emails via both POP3 and IMAP protocols. Please note that reading emails from Gmail using these scripts requires you to set up a custom App password. Gmail treats these scripts as third-party email clients, and for security reasons, you cannot use your regular Gmail password. 

## Prerequisites

Before using these scripts, make sure you have the following:

- Python 3.x installed on your machine.
- Access to the email account you want to read emails from.
- For Gmail, you must enable IMAP and generate an App Password (for both scripts) if you have two-factor authentication enabled.

## Usage

### POP3 Email Client

This script uses the POP3 protocol to read emails. Replace the following placeholders in the script with your own email and server details:

- `EMAIL_ADDR`: Your email address.
- `EMAIL_PASS`: Your App Password (for Gmail).
- `IMAP_ADDR`: Address of your POP3 server.
- `SOURCE_EMAIL_ADDR`: The email address you want to search for.

Run the script to fetch and print email content.

```python
from poplib import POP3_SSL

# ... (rest of the code)
```

### IMAP Email Client

This script uses the IMAP protocol to read emails. Replace the following placeholders in the script with your own email and server details:

- `EMAIL_ADDR`: Your email address.
- `EMAIL_PASS`: Your App Password (for Gmail).
- `IMAP_ADDR`: Address of your IMAP server.
- `SOURCE_EMAIL_ADDR`: The email address you want to search for.

Run the script to fetch and print email content.

```python
from imaplib import IMAP4_SSL

# ... (rest of the code)
```

## Gmail App Password

**Important:** To read emails from Gmail using these scripts, you must generate an "App Password" for your Gmail account. This password is specific to these email client scripts and is used instead of your regular Gmail password. You can generate an App Password in your Gmail account settings. Please ensure that you follow the security guidelines provided by Gmail for generating and managing App Passwords.

