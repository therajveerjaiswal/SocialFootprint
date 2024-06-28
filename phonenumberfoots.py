from time import time
import time
import phonenumbers 
from phonenumbers import timezone, geocoder, carrier
import sys 
from colorama import Fore
import requests

def phone_number_info():

    api_key = input('>> Enter your(NumLook) API key:').strip()

    while True:
        user_number = input('>> Enter a number with country code: ').strip()
        
        try:
            phoneNumber = phonenumbers.parse(user_number)
            
            Carrier = carrier.name_for_number(phoneNumber, 'en')
            Region = geocoder.description_for_number(phoneNumber, 'en')
            
            print(Fore.GREEN + '>> Number you entered is:', user_number)
            time.sleep(2)
            print(Fore.GREEN + '>> Service provider is:', Carrier)
            time.sleep(2) 
            print(Fore.GREEN + '>> Region is:', Region)
            print(Fore.RESET + '')
            
            response = requests.get(f"https://api.numlookupapi.com/v1/validate/{user_ka_number}?apikey={api_key}")
            if response.status_code == 200:
                data = response.json()
                state = data.get('location', 'Unknown')
                print(Fore.GREEN + f">> The state for the phone number is: {state}")
                print(Fore.RESET+"")
            else:
                print(Fore.RED + f"Failed to retrieve information: {response.status_code}")
                print(Fore.RESET+"")
            
        except phonenumbers.NumberParseException:
            print(Fore.RED + ">> The phone number entered is not valid. Please try again.")
            print(Fore.RESET+"")
        
        perm = input('Do you want to operate again? (y/n): ').lower()
        if perm != 'y':
            sys.exit()
if __name__=='__main__':
    print()
