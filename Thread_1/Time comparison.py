import time
from threading import Thread


def d2(n):
    for x in n:
        time.sleep(1)
        print(x % 2)


def d3(n):
    for x in n:
        time.sleep(1)
        print(x % 3)


n = [2, 3, 4, 6, 7]
s = time.time()
# d2(n)                                 # spent 10 sec
# d3(n)
t1 = Thread(target=d2, args=(n,))       # spent 5 sec
t2 = Thread(target=d3, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()

e = time.time()
print(e - s)
print(time.time() - s)

