from multiprocessing import Process, Value, Array, Lock
import time


def add_100(lock, number):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()              # if used acquire  always  used release  after!!!!!
        number.value += 1
        lock.release()

# or we use contextmanager
#         with lock:
#             number.value += 1


if __name__ == "__main__":
    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(lock, shared_number))  # WAR koma - needs here that Python knows - is tuple
    p2 = Process(target=add_100, args=(lock, shared_number))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is', shared_number.value)

# We have different results 130 or 138 or 136
# It's happened because we have race condition occurs - two or more processes try to access to the same shared variable in the same time

# To privent this we must used Lock ( import from multiprocessing)
