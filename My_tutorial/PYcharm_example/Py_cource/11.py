munbers=[]
def foo (num):
    munbers=[]
    for i in range(1, num + 1):
        if i%3 == 0 and i%5 == 0 :
            munbers.append('FizzBazz')
            print("FizzBazz")
        elif i%3 == 0:
            munbers.append('Fizz')
            print("Fizz")
        elif i%5 == 0 :
            munbers.append('Bazz')
            print("Bazz")
        else:
            munbers.append(str(i))
            print(str(i))
    return munbers
            
print ("foo(6) -> ", foo(6))   
#print("munbers: ", munbers[])

assert foo(6) == ["1", "2", "Fizz", "4", "Bazz", "Fizz"]
#assert foo(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]
