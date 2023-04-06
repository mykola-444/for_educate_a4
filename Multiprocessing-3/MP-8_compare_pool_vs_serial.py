import time
from multiprocessing import Pool


def sum_square(num):
    s = 0
    for i in range(num):
        s += i * i
    return s


def sum_square_with_mp(num):
    start = time.time()
    p = Pool()                          # if we used Pool() - default proc_mun = os.cpu_count()
    result = p.map(sum_square, num)

    p.close()
    p.join()

    end = time.time() - start
    print(f' Processing {len(num)} numbers took {end} time using multiprocessing')


def sum_square_no_mp(num):
    start = time.time()
    result = []
    for i in num:
        result.append(sum_square(i))

    end = time.time() - start
    print(f' Processing {len(num)} numbers took {end} time using serial processing')


if __name__ == "__main__":
    num = range(10000)
    sum_square_with_mp(num)
    sum_square_no_mp(num)

# Result
# Processing 100 numbers took 0.3809998035430908 time using multiprocessing
# Processing 100 numbers took 0.0 time using serial processing
# Processing 1000 numbers took 0.3758120536804199 time using multiprocessing
# Processing 1000 numbers took 0.021000385284423828 time using serial processing
# Processing 10000 numbers took 0.9689996242523193 time using multiprocessing
# Processing 10000 numbers took 1.9830679893493652 time using serial processing

# we must use multiprocessing for hard tasks