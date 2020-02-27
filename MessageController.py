import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

class MessageController:
    def send_sms(self,receivers):
        account_sid = 'ACe6d8fd9795d0ba551ec3f98d8c527ae6'
        auth_token = '1549d0fc0df115768a21b14c06de17a8'
        client = Client(account_sid, auth_token)
        '''
        message = client.messages \
            .create(
            body="Emergency SOS: Tesla Song called emergency service after Deepcare detected a hard fall. You receive this email because Tesla listed you as an emergency contact.\nLocation: https://goo.gl/maps/at836pE7yXf5tDkR9",
            from_='+17759904758',
            to=receivers
        )
        '''
        numbers_to_message = receivers
        for number in numbers_to_message:
            message = client.messages.create(
                body = "Emergency SOS: Tesla Song called emergency service after Deepcare detected a hard fall. You receive this email because Tesla listed you as an emergency contact.\nLocation: https://goo.gl/maps/at836pE7yXf5tDkR9",
                from_ = '+17759904758',
                to = number
            )
            print(message.sid)

    def send_warningMsg(self,receivers):
        sender = 'utsiotlab@gmail.com'
        msg = MIMEText("""Tesla Song called emergency service after Deepcare detected a hard fall. You receive this email because Tesla listed you as an emergency contact.\nLocation: https://goo.gl/maps/at836pE7yXf5tDkR9""")
        msg['Subject'] = "Test: Emergency SOS"
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login('utsiotlab@gmail.com', 'gta8875833')
            smtp.sendmail(sender, receivers, msg.as_string())
            print("Successfully sent email")
        except smtplib.SMTPException:
            print("Error: unable to send email")