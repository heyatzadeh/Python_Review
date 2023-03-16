from twilio.rest import Client
import config

client = Client(config.twilio_SID, config.twilio_Auth_Token)
message = client.messages.create(
    body="Who is messaging me?",
    from_="+15076695290",
    to="+989383808566"
)

print(message.sid)
