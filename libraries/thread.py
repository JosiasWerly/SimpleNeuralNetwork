import threading
import time

class ThreadCounter():
    def __init__(self):
        self.Thread = None
        self.Counter = 10
        self.tSleep = 1

    def start(self):
        print("starting")
        if self.Thread != None:
            self.Thread.join()
            self.Thread = None
        self.Thread = threading.Thread(target=self.tick)
        self.Thread.start()
    def stop(self):
        self.Thread.join()
    def tick(self):
        while True:
            for x in range(0, self.Counter):
                print(x)
            print("\tsleeping", self.tSleep)
            time.sleep(self.tSleep)