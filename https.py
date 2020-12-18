import requests


##request connection
s = requests.Session()
s.verify = '/home/nial/newP/pelayan.pem'

req = requests.get('https://192.168.1.27:443'
		, verify='/home/nial/newP/pelayan.pem')

print(req)

z = input('\n Data Retrived!! Please name it: ')
with open (z,'w') as f:
	f.write(req.text)





s.close()
