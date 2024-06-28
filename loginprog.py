import sys
from colorama import Fore
def login(username,password):
   save_usr='socialfootprint'
   save_pass='devpythonraz'
   
   if(username==save_usr and password==save_pass):
    print(Fore.GREEN+'--> You have logged in')
    print(Fore.YELLOW+'[*] Session Opened')
    print(Fore.RESET+'')
    
   
   
   elif(username!=save_usr and password!=save_pass):
        print(Fore.RED+'--> Sorry, incorrect Username or Password')
        print(Fore.RESET+'')
        sys.exit('>> You cannot proceed furthur,read the rules if you dont know the Username and Password')
        
if __name__=='__main__':
    print()