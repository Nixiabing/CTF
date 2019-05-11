import base64

playload = 0
data = ""
str = "fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA="
s = base64.b64decode(str)
key = "729623334f0aa2784a1599fd374c120d"
x = 0
ch = "729623334f0aa2784a1599fd374c120d729623"
#playload += ((s[0]) - ord(ch[0])%128)
for i in range(38):
    playload = ((s[i]) - ord(ch[i]))
    if playload < 0:
        playload += 128
    data += chr(playload)
print(data)