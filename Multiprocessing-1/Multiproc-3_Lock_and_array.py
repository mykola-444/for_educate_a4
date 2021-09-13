# here we improve the previous file using array 
from multiprocessing import Process, Value, Array, Lock
import time


def add_100(lock, numbers):
    for i in range(100):
        time.sleep(0.01)
# this not good because loop use whole array - not 1 by 1  !!!!!!!!!!!
#         for number in numbers:
#             number += 1
        for i in range(len(numbers)):             # don't forget about race_conditions
            with lock:
                numbers[i] += 1



if __name__ == "__main__":
    lock = Lock()
    # instead value use Arrey
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning is', shared_array[:])  #use slicing here

    p1 = Process(target=add_100, args=(lock, shared_array))  # WAR koma - needs here that Python knows - is tuple
    p2 = Process(target=add_100, args=(lock, shared_array))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at end is', shared_array[:])



