# in video import threading - not correct
#import threading
from threading import *


class MyThread(Thread):
    def run(self):
        for x in range(7):
            print("chaild = ", current_thread().getName())


obj = MyThread()
obj.start()
obj.join()

print("Control returned to ", current_thread().getName())
