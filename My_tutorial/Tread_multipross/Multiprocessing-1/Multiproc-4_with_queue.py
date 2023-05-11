# here we improve the previous file using Queue
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time


def square(q, numbers):
    for i in numbers:
        q.put(i * i)


def make_negative(q, numbers):
    for i in numbers:
        q.put(-1 * i)


if __name__ == "__main__":
    numbers = range(1, 6)
    q = Queue()
    p1 = Process(target=square, args=(q, numbers))
    p2 = Process(target=make_negative, args=(q, numbers))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
