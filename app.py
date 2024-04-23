import pywhatkit

# Taking user input
phone_number = input("Enter the phone number (with country code): ")
message = input("Enter the message you want to send: ")
hour = int(input("Enter the hour (24-hour format) when you want to send the message: "))
minute = int(input("Enter the minute when you want to send the message: "))

# Sending the message
pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
