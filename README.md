# captchaCodeMakerV2
Make Roblox's signup funcaptcha code so you can send to discord bots (REMADE)

### Example on how to get the code after
Better example [link](https://github.com/Roblox-Thot/captchaCodeMakerV2/blob/main/example/sign%20up.py)
```py
import base64
code = "Code here"
decoded = base64.b64decode(code).split(b',')
captchaId = decoded[0]
captchaToken = decoded[1]
print(f'Captcha ID: {captchaId}')
print(f'Captcha Token: {captchaToken}')
```
