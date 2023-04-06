import multiprocessing as mp
import time


def foo_pool(x):
    time.sleep(1)
    # print(x*x)
    return x * x


result_list = []


def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


def apply_async_with_callback():
    pool = mp.Pool()
    for i in range(10):
        pool.apply_async(foo_pool, args=(i,), callback=log_result)
        #pool.apply(foo_pool, args=(i,))
    pool.close()
    pool.join()
    print(result_list)
    # every time we have different result it depends from order of process
    # [0, 4, 1, 9, 16, 36, 25, 49, 64, 81]
    # [0, 1, 4, 9, 16, 36, 25, 49, 64, 81]
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    # [1, 0, 9, 4, 16, 25, 36, 49, 81, 64]


if __name__ == '__main__':
    apply_async_with_callback()
