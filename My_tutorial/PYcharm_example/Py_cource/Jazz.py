def foo(num):
    numbers = []
    for i in range(90, num + 1):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            numbers.append('FizzBazzJazz')
        elif i % 3 == 0 and i % 5 == 0:
            numbers.append('FizzBazz')
        elif i % 3 == 0 and i % 7 == 0:
            numbers.append('FizzJazz')
        elif i % 5 == 0 and i % 7 == 0:
            numbers.append('BazzJazz')
        elif i % 3 == 0:
            numbers.append('Fizz')
        elif i % 5 == 0:
            numbers.append('Bazz')
        elif i % 7 == 0:
            numbers.append('Jazz')
        else:
            numbers.append(str(i))
    return numbers


assert foo(105) == ['FizzBazz', 'Jazz', '92', 'Fizz', '94', 'Bazz', 'Fizz', '97', 'Jazz', 'Fizz', 'Bazz', '101', 'Fizz', '103', '104', 'FizzBazzJazz']
