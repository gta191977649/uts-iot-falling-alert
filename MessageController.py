import smtplib
from email.mime.text import MIMEText

class MessageController:

    def send_warningMsg(self,receivers):
        sender = 'episodes27@gmail.com'

        msg = MIMEText("""The falling detection may occur""")
        msg['Subject'] = "Test: Alert From Miniwave radar"
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login('episodes27@gmail.com', 'lb091010965')
            smtp.sendmail(sender, receivers, msg.as_string())
            print("Successfully sent email")
        except smtplib.SMTPException:
            print("Error: unable to send email")