#https://www.youtube.com/watch?v=fKl2JW_qrso
import multiprocessing
import time


def do_something():
    print('Sleeping 1 s')
    time.sleep(1)
    print('Done sleeping')


if __name__ == "__main__":                              # strange!!! don't work without this
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')
