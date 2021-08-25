from threading import *


class Ex():
    def myfunc(self):
        my_list=[2,1,'w',8.7,'abs']
        for x in my_list:
            print("Chaild",x)


my_obj = Ex()
thread1 = Thread(target=my_obj.myfunc)
thread1.start()
thread1.join()
print("Done")



