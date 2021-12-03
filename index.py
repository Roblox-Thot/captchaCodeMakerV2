from flask import Flask, render_template
from wonderwords import RandomWord
import requests, base64, random
app = Flask(__name__)
r = RandomWord()

#region Roblox

# Get current Public keys
funCaptchaPublicKeys = requests.get("https://apis.rbxcdn.com/captcha/v1/metadata").json()["funCaptchaPublicKeys"]

def getXsrf():
    '''
    Fuck Roblox's Cross-site request forgery shit

    Returns X-Csrf-token
    '''
    xsrHeader = requests.post("https://auth.roblox.com/v2/login", headers={
        "X-CSRF-TOKEN": ""
    }).headers['x-csrf-token']
    return xsrHeader


def getFieldData():
    '''
    Get the field data code thingy That Roblox uses for captchas now

    Returns the field data token used in captchas
    '''
    headers = {
        'authority': 'auth.roblox.com',
        'x-csrf-token': getXsrf(),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
    }

    return requests.post('https://auth.roblox.com/v2/signup', headers=headers, json={}).json()["failureDetails"][0]["fieldData"]

#endregion

@app.route('/', methods=['GET'])
def hello_world():
    '''
    Renders out the captcha page when user goes to main page.
    '''

    '''
    data[0] = captchaId
    data[1] = captchaData (unused in creating/logging into accounts'''
    data = getFieldData().split(',')

    # Give the user the captcha page
    return render_template('getcode.html',
                            funCaptchaPublicKeys = funCaptchaPublicKeys["ACTION_TYPE_WEB_SIGNUP"],
                            message = "Solve captcha to get the code!",
                            data = str( data[1]),
                            id = data[0]
                        )

# run flask i guess
if __name__ == '__main__':
    app.run()
