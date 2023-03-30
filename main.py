from sys import argv
from time import sleep
from worker import Worker
import signals

def getFile(args) -> list:
    if len(args) < 2:
        raise ValueError()
    filename = args[1]
    if filename == None:
        raise ValueError()
    moduleList = []
    file = open(filename, 'r').read().splitlines()
    for line in file:
        moduleList.append(line)
    return moduleList

def main(moduleList: list):
    workers = []
    print('creating workers')
    for w in moduleList:
        workers.append(Worker(w))
    print('starting workers')
    for w in workers:
        w.start()
    while True: sleep(60)

if __name__ == '__main__':
    try:
        main(getFile(argv))
    except ValueError:
        print("invalid arguments")
    except FileNotFoundError:
        print("file not found")
    except(KeyboardInterrupt, SystemExit):
        print("sending stop signal")
        signals.stop_signal = 1
    except:
        print("unexpected error")
