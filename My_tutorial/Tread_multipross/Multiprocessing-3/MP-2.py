#https://www.youtube.com/watch?v=fKl2JW_qrso
import multiprocessing
import time


def do_something(sec):
    print(f'Sleeping {sec} s')
    time.sleep(sec)
    print('Done sleeping')


if __name__ == "__main__":
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        #p = multiprocessing.Process(target=do_something, args=[2])          #!!!!!!!!!the same
        p = multiprocessing.Process(target=do_something, args=(2,))
        p.start()
    processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')
