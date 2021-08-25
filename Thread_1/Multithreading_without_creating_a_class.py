from threading import *


def new():
    for x in range(6):
        print("child executing..", current_thread().getName())


t1 = Thread(target=new)
# we will have "Bya MainThread"
print(current_thread().getName())
t1.start()
t1.join()  # without join "Bya" after first "child executing.." > with join  in the end

# we will have "Bya MainThread" also
print("Bya", current_thread().getName())
