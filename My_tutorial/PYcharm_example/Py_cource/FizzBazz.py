def foo(num):
    numbers=[]
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append('FizzBazz')
        elif i%3 == 0:
            numbers.append('Fizz')
        elif i%5 ==0:
            numbers.append('Bazz')
        else:
            numbers.append(str(i))
    return numbers




assert foo(6) == ["1", "2", "Fizz", "4", "Bazz", "Fizz"]

