'''\
Генерация и вывод чисел Фибоначчи
'''
def fib(n):
    '''Выводит последовательность чисел Фибоначчи,
    не превышающих n'''
    a, b = 0, 1
    while b < n:
        print (b),
        a, b = b, a+b
fib(15)



def fib2(n):
    '''Возвращает список, содержащий числа ряда
    Фибоначчи, не превышающие n'''
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print (fib2(129))

