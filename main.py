from threading import Thread
import scenarios.webgoat_sample as wg

if __name__ == '__main__':
    t1 = Thread(target=wg.run, args=["t1",])
    t2 = Thread(target=wg.run, args=["t2",])

    t1.start()
    t2.start()