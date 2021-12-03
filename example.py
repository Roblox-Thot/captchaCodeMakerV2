# This code could be improved but its just a example on how to use the code from the site

import requests, base64, random, string
try:
    import pyperclip
except:
    pass

token = input("Put code from https://roblox-thot.github.io/captchaCodeMaker/ here:\n")

headers = {
    'authority': 'auth.roblox.com',
    'dnt': '1',
    'x-csrf-token': requests.post("https://auth.roblox.com/v2/login").headers["x-csrf-token"],
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
}

username = ''.join(random.choice(string.ascii_letters) for i in range(20))

tokens = base64.b64decode(token).split(',')
data = {
    "username":username,
    "password":username[::-1],
    "birthday":"01 Oct 2003",
    "gender":1,
    "isTosAgreementBoxChecked":True,
    "context":"MultiverseSignupForm",
    "referralData":None,
    "displayAvatarV2":False,
    "displayContextV2":False,
    "captchaId":tokens[0],
    "captchaToken":tokens[1],
    "captchaProvider":"PROVIDER_ARKOSE_LABS",
    "agreementIds":["54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3","848d8d8f-0e33-4176-bcd9-aa4e22ae7905"]
}

response = requests.post('https://auth.roblox.com/v2/signup', headers=headers, json=data)
# Debug
#print(response)
#print()
#print(response.text)
#print()

try:
    cookie = response.cookies[".ROBLOSECURITY"]
    print()
    print(f'login: {username}:{username[::-1]}')
    print(f'\nCookie:\n{cookie}')
    try: #trys to copy the cookie if you have pyperclip installed
        pyperclip.copy(cookie)
    except:
        pass
except:
    print("Failed to create")
    pass
