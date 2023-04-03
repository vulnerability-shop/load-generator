import requests
import time

def main():
    host = "http://127.0.0.1:5180"
    
    s = requests.Session()
    
    data = { 'username':'admin', 'password':'password' }
    
    r = s.post(host + "/login", json=data)

    print(str(r))
    print(r.reason)
    print(s.cookies)

if __name__ == '__main__':
    main()