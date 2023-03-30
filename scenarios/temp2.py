import requests
import time

def main():
    host="http://127.0.0.1:8080/WebGoat"

    s = requests.Session()

    params = { 'username':'admin1', 'password':'admin1' }
    r = s.post(host + "/login", params=params)
    print(str(r.status_code))
    time.sleep(1)

    r = s.get(host + "/SqlInjection.lesson.lesson")
    print(str(r.status_code))
    time.sleep(1)

    params = { 'query':"select department from Employees where first_name='Bob'" }
    r = s.post(host + "/SqlInjection/attack2", params=params)
    print(str(r.status_code))
    time.sleep(1)

if __name__ == '__main__':
    main()
