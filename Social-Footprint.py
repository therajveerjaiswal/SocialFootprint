limport loginprog
import sys
from colorama import Fore
import mechanism as mec
import phonenumberfoots as phnmf

print(Fore.YELLOW+'>> Social Footprint V1.0\n>> [Author:Rajveer]')
print(Fore.RESET+'')
option_usr=input('1. Read Rules\n2. Start the program >>>')


if(option_usr=='1'):
    rules=open('Howto.txt','r')
    rules_read=rules.readlines()
    print(rules_read)
    rules.close()
    sys.exit()


elif(option_usr=='2'):
    print(Fore.GREEN+'[*] Verify Authentication')
    print(Fore.RESET+'')
    username=input('Enter Username:')
    password=input('Enter Password:')
    loginprog.login(username,password)
    print('>> Options')
    print('[1] Instagram')
    print('[2] Terminal Phone Check')
    choose=input('>> ')
    if choose == '1':
        username=input('>> Enter Username:')
        mec.check_instagram_user(username)
    elif choose=='2':
        phnmf.phone_number_info()

    