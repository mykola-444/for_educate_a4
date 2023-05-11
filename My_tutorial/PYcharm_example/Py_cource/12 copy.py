munbers=[]
def get_val(i):
    divided_by_3 = (i % 3 == 0)
    divided_by_5 = (i % 5 == 0)
    divided_by_7 = (i % 7 == 0)
    val = ""
    if divided_by_3:
        val = "Fizz"
    if divided_by_5:
        val = val + "Bazz"
    if divided_by_7:
        val += "Jazz"
    if not val:
        val = str(i)
    return val

def foo (n):
    numbers = []
    for i in range(1, n+1):
        val = get_val(i)
        numbers.append(val)
    return numbers


assert get_val(1) == "1"
assert get_val(5) == "Bazz"
assert get_val(7) == "Jazz"
assert get_val(14) == "Jazz"
assert foo(15) == ["1", "2", "Fizz", "4", "Bazz", "Fizz","Jazz","8","Fizz","Bazz","11","Fizz","13","Jazz","FizzBazz"]
