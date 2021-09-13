# https://www.youtube.com/watch?v=fKl2JW_qrso
import concurrent.futures
import time


def sleep(sec):
    print(f'Sleeping {sec} s')
    time.sleep(sec)
    return f'Done sleeping ... {sec}'


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        result = [executor.submit(sleep, sec) for sec in secs]

        for f in concurrent.futures.as_completed(result):       # as_completed method - return result
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')
