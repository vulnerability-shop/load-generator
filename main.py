from sys import argv
from time import sleep
from worker import Worker
import signals

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
    try:
        if len(argv) < 2:
            raise ValueError()
        filename = argv[1]
        if filename == None:
            raise ValueError()
        moduleList = []
        file = open(filename, 'r').read().splitlines()
        for line in file:
            moduleList.append(line)
        main(moduleList)
    except ValueError:
        print("invalid arguments")
    except FileNotFoundError:
        print("file not found")
    except:
        print("unexpected error")
