import phonenumbers
from phonenumbers import geocoder

phone = input('Insert the phone number [+DDIDDNNNNNNNNN]: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
