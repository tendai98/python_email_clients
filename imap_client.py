from imaplib import IMAP4_SSL

emails = []

EMAIL_ADDR = 'projectsiot9@gmail.com'	# Stores target email address
EMAIL_PASS = 'ifwa kuog kjjy pfxe'	# Stores password to email address (Gmails requires unique App password for this email client script)
IMAP_ADDR = 'imap.gmail.com'		# Adress of IMAP server

SOURCE_EMAIL_ADDR = 'team@m.ngrok.com'	# Target source email we want to use for search

mail_client = IMAP4_SSL(IMAP_ADDR)	# Connect to the IMAP Server
mail_client.login(EMAIL_ADDR, EMAIL_PASS)	# Authenticate with the IMAP Server
mail_client.select('Inbox')	# Set source to 'Inbox'

# Run query on mail box
status, data = mail_client.search(None, 'FROM', '"{}"'.format(SOURCE_EMAIL_ADDR))

if(status == 'OK'):

	for index in data[0].split():
		# Fetch email data based on returned email indices
		status, data = mail_client.fetch(index, '(RFC822)')
		# Append each of the email raw text to a list
		emails.append(data)



# Select one email and loop through its fields
for field in emails[0][0]:
	# Decode the data to text since its in byte form
	print(field.decode())
