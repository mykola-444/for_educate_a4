# import threading
import concurrent.futures
import time

start = time.perf_counter()


# with arrguments
def do_something(second):
    print(f'Sleeping {second} sec')
    time.sleep(second)
    return f'Done sleeping {second}'


# with concurrent.futures.ThreadPoolExecutor() as execotor:
#     f1 = execotor.submit(do_something, 1)
#     f2 = execotor.submit(do_something, 1)
#
#     print(f1.result())
#     print(f2.result())

# *** with coprehention and only one arrgument
# with concurrent.futures.ThreadPoolExecutor() as execotor:
#     results = [execotor.submit(do_something, 1) for _ in range(10)]

with concurrent.futures.ThreadPoolExecutor() as execotor:
    secs = [5, 4, 3, 2, 1]
    results = [execotor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finishing in {round(finish - start, 3)} sec')
