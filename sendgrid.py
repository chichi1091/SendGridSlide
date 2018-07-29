# -*- coding:utf-8 -*-

import sendgrid
from sendgrid.helpers.mail import *

api_key = 'xxxxxxxxxxxxxxxxxx'
sg = sendgrid.SendGridAPIClient(apikey=api_key)
 
mail = Mail()
mail.from_email = Email("chichi.pa2.1091@gmail.com")
personalization = Personalization()
personalization.add_to(Email("chichi.pa2.1091@gmail.com"))
personalization.subject = "[SendGrid]テストメール"
mail.add_personalization(personalization)
mail.add_content(Content("text/plain", "test test\n\rテスト　テスト"))
response = sg.client.mail.send.post(request_body=mail.get())
 
print(response.status_code)
print(response.body)
print(response.headers)