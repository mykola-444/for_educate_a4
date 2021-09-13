from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

# map,apply,join,close  - four important methods
    result = pool.map(cube, numbers)

    #res = pool.apply(cube, numbers[5:])      #argument after CUBE must be an iterable, not int

    pool.close()
    pool.join()
    print(result)

