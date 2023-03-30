from threading import Thread
import scenarios.webgoat_sample as wg
import scenarios.scenario_sample as ss
import scenarios.temp as t
#from config import stop_signal
import signals
from time import sleep
import importlib
from worker import Worker

def main(moduleList: list):
    try:
        workers = []
        print('creating workers')
        for w in moduleList:
            workers.append(Worker(w))
        print('starting workers')
        for w in workers:
            w.start()
        while True: sleep(60)
    except(KeyboardInterrupt, SystemExit):
        print("sending stop signal")
        signals.stop_signal = 1

if __name__ == '__main__':
    moduleList = []
    file = open('script1.txt', 'r').read().splitlines()
    for line in file:
        moduleList.append(line)
    main(moduleList)

    #webgoat_sample
    #t1 = Thread(target=wg.run, args=["t1",])
    #t2 = Thread(target=wg.run, args=["t2",])
    #t1.daemon = True
    #t2.daemon = True


    ##scenario_sample
    #s1 = ss.Scenario("s1")
    #s2 = ss.Scenario("s2")
    #t1 = Thread(target=s1.run)
    #t2 = Thread(target=s2.run)
    #try:        
    #    t1.start()
    #    t2.start()
    #except(KeyboardInterrupt, SystemExit):
    #    #s1.stop()
    #    #s2.stop()
    #    pass
    #print("press ctrl+c to stop")
    #input("")


    #thread subclass
    #s1 = ss.Scenario("s1")
    #s2 = ss.Scenario("s2")
    #try:
    #    s1.start()
    #    s2.start()
    #    #s1.join()
    #    #s2.join()
    #except(KeyboardInterrupt, SystemExit):
    #    print("stopping")
    #    s1.stop()
    #    s2.stop()


    #test
    #t1 = t.Scenario("t1")
    #t2 = t.Scenario("t2")
    #t1.daemon = True
    #t2.daemon = True
    #try:
    #    t1.start()
    #    t2.start()
    #    while True: time.sleep(100)
    #except(KeyboardInterrupt, SystemExit):
    #    print("sending stop signal")
    #    stop_signal = 1


    #test2
    #try:
    #    w1 = Worker('scenarios.temp2')
    #    w2 = Worker('scenarios.temp2')
    #    w1.start()
    #    w2.start()
    #    while True: time.sleep(100)
    #except(KeyboardInterrupt, SystemExit):
    #    print("sending stop signal")
    #    stop_signal = 1

    