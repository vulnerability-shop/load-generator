from importlib import import_module
from threading import Thread
import signals

class Worker(Thread):
    def __init__(self, module_name):
        super().__init__()
        self.m = import_module(module_name)
    def run(self):
        while True:
            if signals.stop_signal:
                exit()
            self.m.main()
