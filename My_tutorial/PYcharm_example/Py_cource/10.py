def foo (num):
    for i in range(1, num+1, 1):
        if i%3 == 0 and i%5 == 0 :
           print("FizzBazz")
           continue
        else:
           if i%3 == 0:
               print("Fizz")
               continue
           else:
              if i%5 == 0 :
                  print("Bazz")
                  continue
              else:    
                 print (str(i))
      
print (foo(15))   
