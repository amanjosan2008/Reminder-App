from twilio.rest import Client
from myapp.models import message_format
import os


def sms(name,phone):

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    Message = str(message_format.objects.latest('id'))
    First_part = Message.split('%s')[0]
    Last_part = Message.split('%s')[-1]
    Body = First_part + name + Last_part
    To='+91'+'%s' %phone

    message = client.messages.create(
             body=Body,\
             from_='+15103984676',\
             to=To)
    return message.sid

