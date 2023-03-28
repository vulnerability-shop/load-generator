from threading import Thread
import scenarios.webgoat_sample as wg
import scenarios.scenario_sample as ss

if __name__ == '__main__':

    #webgoat_sample
    #t1 = Thread(target=wg.run, args=["t1",])
    #t2 = Thread(target=wg.run, args=["t2",])
    #t1.daemon = True
    #t2.daemon = True

    #scenario_sample
    s1 = ss.Scenario("s1")
    s2 = ss.Scenario("s2")

    t1 = Thread(target=s1.run)
    t2 = Thread(target=s2.run)

    try:        
        t1.start()
        t2.start()
    except(KeyboardInterrupt, SystemExit):
        #s1.stop()
        #s2.stop()
        pass

    print("press ctrl+c to stop")
    input("")

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