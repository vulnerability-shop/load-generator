#from requests2 import http_legit
#r = http_legit.do_http_basic("http://10.0.2.4/")
#print(r)

#from request_types import nmap_basic
#nmap_basic.scan_all_ports('10.0.2.4')

import requests

host="http://10.0.2.5:8080/WebGoat"

s = requests.Session()

#params = { 'username':'webgoat', 'password':'webgoat', 'matchingPassword':'webgoat', 'agree':'agree' }
#r = s.get(host + "/register.mvc")
#print(r)

params = { 'username':'webgoat', 'password':'webgoat' }
r = s.post(host + "/login", params=params)
print(r)

r = s.get(host + "/SqlInjection.lesson.lesson")
print(r)

params = { 'query':"select department from Employees where first_name='Bob'" }
r = s.post(host + "/SqlInjection/attack2", params=params)
print(r.text)
