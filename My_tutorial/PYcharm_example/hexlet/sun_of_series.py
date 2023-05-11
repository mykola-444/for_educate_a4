def sum_of_series(start, finish):
    result = 0
    n = start
    while n <= finish:
        result += n
        n += 1
    return result

print(sum_of_series(3,4))

