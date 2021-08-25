import threading
import time

start = time.perf_counter()


# without arrgument
# def do_something():
#     print("Sleeping 1 sec")
#     time.sleep(1)
#     print('Done sleeping')

# with arrguments
def do_something(second):
    print(f'Sleeping {second} sec')
    time.sleep(second)
    print('Done sleeping')


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finishing in {round(finish - start, 3)} sec')
