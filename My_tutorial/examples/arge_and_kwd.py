*args
# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It # is used to pass a non-keyworded, variable-length argument list.
# Python program to illustrate   
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  
Output:
Hello
Welcome
to
GeeksforGeeks

# Python program to illustrate  
# *args with first extra argument 
def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
Output:
First argument : Hello
Next argument through *argv : Welcome
Next argument through *argv : to
Next argument through *argv : GeeksforGeeks

**kwargs
# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

# Python program to illustrate   
# *kargs for variable number of keyword arguments 
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')     
Output:
last == Geeks
mid == for
first == Geeks

# Python program to illustrate  **kargs for  
# variable number of keyword arguments with 
# one extra argument. 
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
 
# Driver code 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')     
Output:
last == Geeks
mid == for
first == Geeks






def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3)  
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Geeks", "for", "Geeks") 
myFun(*args) 
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 
Output:
arg1: Geeks
arg2: for
arg3: Geeks
arg1: Geeks
arg2: for

def myFun(*args,**kwargs): 
    print("args: ", args) 
    print("kwargs: ", kwargs)  
# Now we can use both *args ,**kwargs to pass arguments to this function : 
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks") 
Output:
args: ('geeks', 'for', 'geeks')
kwargs {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}


