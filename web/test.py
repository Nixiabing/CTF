import requests
import time

url_all = open("url",'r').readlines()
f = open("out","w+")

headers = {
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Accept-Encoding': "gzip, deflate",
    'Referer': "http://am.echargenet.com/",
    'Connection': "close",
    'cache-control': "no-cache"
    }

for u in url_all:
    u = "http://" + u.replace('\n', '')

    try:
        response = requests.request("GET", u, headers=headers,timeout=10)
        print(response.status_code)
        if response.status_code == 200:
            if "nginx" in response.text:
                f.write(u)
        time.sleep(1)

    except requests.exceptions.ConnectionError:
        print("ssl worng~")
    except requests.exceptions.ReadTimeout:
        print("timeout!!")
    except UnicodeError:
        print("UnicodeError???")