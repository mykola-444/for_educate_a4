#https://www.youtube.com/watch?v=fKl2JW_qrso
import concurrent.futures
import time


def sleep(sec):
    print(f'Sleeping {sec} s')
    time.sleep(sec)
    return 'Done sleeping'


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(sleep, 1)              # the same (target=do_something, args=[1.5]
        f2 = executor.submit(sleep, 1)
        # if we use this structure we make change in function and RETURN something
        print(f1.result())
        print(f2.result())

    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something)  # like in thread we also use args
    #     p.start()
    # processes.append(p)
    #
    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')
