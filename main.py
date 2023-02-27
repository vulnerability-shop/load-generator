#from requests2 import http_legit
#r = http_legit.do_http_basic("http://10.0.2.4/")
#print(r)

#from request_types import nmap_basic
#nmap_basic.scan_all_ports('10.0.2.4')

import requests

host="http://10.0.2.5:8080/WebGoat/"

def http_get(page):
    url = "{host}{page}".format(host=host,page=page)
    r = requests.get(url=url)
    return r

def http_post(page, json):
    url = "{host}{page}".format(host=host,page=page)    
    r = requests.post(url=url, json=json)
    return r

#print("GET login")
#r = http_get("login/")
#print(r)

#print("POST login")
#json = { 'username':'webgoat', 'password':'webgoat' }
#r = http_post("login/", json)
#print(r)

def test():
    s = requests.Session()

    json = { 'username':'webgoat', 'password':'webgoat' }
    r = s.post("http://10.0.2.5:8080/WebGoat/login/", json=json)
    print("JSESSIONID={cookie}".format(cookie=s.cookies.get("JSESSIONID")))

    cookies = { 'JSESSIONID':s.cookies.get("JSESSIONID") }
    r = s.get("http://10.0.2.5:8080/WebGoat/welcome.mvc", cookies=cookies)
    print (r.text)

    json = { 'query':"select+deprtment+from+Employees+where+first_name='Bob'" }
    r = s.post("http://10.0.2.5:8080/WebGoat/SqlInjection/attack2/", json=json)
    print (r.text)

def test2():
    json = { 'username':'webgoat', 'password':'webgoat' }
    r1 = requests.post("http://10.0.2.5:8080/WebGoat/login", json=json)
    print(r1.text)
    json = { 'query':"select+deprtment+from+Employees+where+first_name='Bob'" }
    r2 = requests.post("http://10.0.2.5:8080/WebGoat/SqlInjection/attack2", json=json, cookies=r1.cookies)
    print(r2.text)

s = requests.Session()
params = { 'username':'webgoat', 'password':'webgoat' }
r = s.post("http://10.0.2.5:8080/WebGoat/login", params=params)
#print(r.text)

params = { 'query':"select+deprtment+from+Employees+where+first_name='Bob'" }
r = s.post("http://10.0.2.5:8080/WebGoat/SqlInjection/attack2", params=params)
print(r.text)
