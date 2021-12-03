# captchaCodeMakerV2
Make Roblox's signup funcaptcha code so you can send to discord bots (REMADE)

### Example on how to get the code after
Will add a better example later!
```py
import base64
code = "Code here"
decoded = base64.b64decode(code).split(',')
captchaId = decoded[0]
captchaToken = decoded[1]
```
