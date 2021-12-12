# captchaCodeMakerV2
Make Roblox's signup funcaptcha code so you can send to discord bots (REMADE)<br>
If this version is giving you a hard time try [mogolicoo's](https://github.com/mogolicoo/captchaCodeMaker) which is made in node.js

### Example on how to get the code after
Better example [link](https://github.com/Roblox-Thot/captchaCodeMakerV2/blob/main/example/sign%20up.py)
```py
import base64
code = "Code here"
decoded = base64.b64decode(code).decode('utf-8').split(',')
captchaId = decoded[0]
captchaToken = decoded[1]
print(f'Captcha ID: {captchaId}')
print(f'Captcha Token: {captchaToken}')
```
