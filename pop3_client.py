from poplib import POP3_SSL

emails = []

EMAIL_ADDR = 'user@domain.com'	# Stores target email address
EMAIL_PASS = 'password'	# Stores password to email address (Gmails requires unique App password for this email client script)
IMAP_ADDR = 'pop.domain.com'		# Adress of POP3 server

SOURCE_EMAIL_ADDR = 'src@domain.com'	# Target source email we want to use for search

mail_client = POP3_SSL(IMAP_ADDR)	# Connect to the POP3 Server
mail_client.user(EMAIL_ADDR)
mail_client.pass_(EMAIL_PASS)	# Authenticate with the POP3 Server

indices = len(mail_client.list()[1])

for i in range(indices):
	for j in mail_client.retr(i+1)[1]:
		print(j)

