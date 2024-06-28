import requests
from bs4 import BeautifulSoup
import webbrowser as wb
import sys

def check_instagram_user(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        
        # Check karega page exist karta hai ya nai
        if response.status_code == 200:
            # Parse karega HTML content ko
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # yaha se usermame se naam extract hoga
            name_tag = soup.find('meta', property='og:title')
            if name_tag and name_tag.get("content"):
                full_name = name_tag.get("content").split("(")[0].strip()
                print(f"User exists. Name: {full_name}")
            else:
                print("User exists, but name not found.")
                take=input('Do you want to view in browser?(y/n):')
                if(take=='y'):
                    wb.open(url)
                elif(take!='y'):
                    sys.exit()
        elif response.status_code == 404:
            print("User does not exist.")
        else:
            print(f"Error: Received unexpected status code {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
if __name__=='__main__':
    print()
