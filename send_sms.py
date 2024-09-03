from twilio.rest import Client

# Your Twilio credentials
account_sid = 'ACe030b767e282529de332d9e61ba5be94'  # Replace with your Account SID
auth_token = '478923d44ce35e1a282a260b5d3e2ad4'    # Replace with your Auth Token

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define message details
message = client.messages.create(
    body='Hello, this is a test message from Twilio!',
    from_='+14439924279',  # Replace with your Twilio phone number
    to='+917498573735'      # Replace with the recipient's phone number
)

# Print message SID to confirm it's sent
print(f"Message SID: {message.sid}")
