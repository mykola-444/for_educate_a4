try:
    x=int(input())
except  ValueError:
    print ("Виввели не число")
    x = 0

try:
    y = int(input())
except  ValueError:
    print ("Виввели не число")
    y = 0
else:
    print ("Все вірно")
finally:
    print ("Виконається на 100")

try:
    res = x/y
except  ZeroDivisionError:
    print ("You tape O")
    res =0
print (res)

 
