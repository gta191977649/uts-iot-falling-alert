from mailjet_rest import Client
import os
api_key = '7a1a7c8d5ae5e72534e321d54af158ae'
api_secret = '37f3aed62eb15a9a841af82915c19043'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "oliverfchen@gmail.com",
        "Name": "fang"
      },
      "To": [
        {
          "Email": "oliverfchen@gmail.com",
          "Name": "fang"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())