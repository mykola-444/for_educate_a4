# calculate the sum of all primes less than 1,000,000. https://habr.com/ru/company/otus/blog/501056/

from multiprocessing import Pool
import time
import os


def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


answer = 0

if __name__ == "__main__":
    start = time.perf_counter()
    # for i in range(1000000):       # for 10 000 000 - 72.87 sec   ( for 1 000 000 - 2,74 sec)
    #     answer += if_prime(i)      # for 10 000 000 - 22.38 sec ( with 8 proc)

    proc_mun = os.cpu_count()       # for my computer max proc_num = 8

    with Pool(4) as p:
        answer = sum(p.map(if_prime, list(range(1000000))))

    # result for number of proc(sec)    2 - 1.85 sec, for 4 -1.25sec, for 8 - 1.03,  for 16 - 1.3, for 24 -1.6sec
    # would be better use  os.cpu_count()  or  half


    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)}')
