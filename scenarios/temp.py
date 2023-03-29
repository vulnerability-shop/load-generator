import requests
import time
import threading
from config import stop_signal

class Scenario(threading.Thread):

    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):

        while(1):

            if stop_signal:
                self.log("stopping")
                exit()

            host="http://127.0.0.1:8080/WebGoat"

            s = requests.Session()

            params = { 'username':'admin1', 'password':'admin1' }
            r = s.post(host + "/login", params=params)
            self.log(str(r.status_code))
            time.sleep(1)

            r = s.get(host + "/SqlInjection.lesson.lesson")
            self.log(str(r.status_code))
            time.sleep(1)

            params = { 'query':"select department from Employees where first_name='Bob'" }
            r = s.post(host + "/SqlInjection/attack2", params=params)
            self.log(str(r.status_code))
            time.sleep(1)

    def log(self, text):
        print(self.thread_name + ': ' + text)