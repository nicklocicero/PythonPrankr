from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account

account_sid = "ACa4b378475d83559789cf9ee93d59c2e3"
auth_token = "6eae2c18b2a74ecb6f9bbaf08635777d"

client = TwilioRestClient(account_sid, auth_token)

class Sms():
    """Twilio sends prank SMS"""

    def __init__(self, sms_title, sms_text):
        self.title = sms_title
        self.text = sms_text

    def send_sms(self, phone_number):
        message = client.messages.create(to="+1"+phone_number, from_="+19292276425",body=self.text)
        print message.sid
