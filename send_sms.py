from twilio.rest import Client


def sms(name,phone):
    #from twilio.rest import Client
    account_sid = 'ACf670adf39d04caa0e8d0fa89309158fd'
    auth_token = '997443bfd22a3486beed7dfbc693a0f7'
    client = Client(account_sid, auth_token)

    Body = 'Dear %s, Your followup with Dentist is due. Kindly plan for a visit.' %name
    To='+91'+'%s' %phone

    message = client.messages.create(
             body=Body,\
             from_='+15103984676',\
             to=To)
    return message.sid
