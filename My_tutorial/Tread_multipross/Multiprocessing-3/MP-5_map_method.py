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
        results = executor.map(sleep, secs)  # MAP runs "sleep" with every items "secs"
        # when we use SUBMIT-method we return future object, but with MAP-method we just return results

        for result in results:     # this only print
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 4)}')
