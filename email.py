from email.message import EmailMessage
import smtplib
import ssl
port = 465  # For SSL
# port can change too
# install suitable packages


subject = "Email From Python"
body = "This is a test email form Python!"
sender_email = "rijulmarhatta@gmail.com"
receiver_email = "rijulmarhatta@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
