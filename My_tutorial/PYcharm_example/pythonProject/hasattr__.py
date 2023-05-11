# Python code to demonstrate
# performance analysis of hasattr()
import time


# declaring class
class GfG:
    name = "GeeksforGeeks"
    age = 24


# initializing object
obj = GfG()

# use of hasattr to check motto
start_hasattr = time.time()
if (hasattr(obj, 'motto')):
    print("Motto is there")
else:
    print("No Motto")

print("Time to execute hasattr : " + str(time.time() - start_hasattr))

# use of try/except to check motto
start_try = time.time()
try:
    print(obj.motto)
    print("Motto is there")
except AttributeError:
    print("No Motto")
print("Time to execute try : " + str(time.time() - start_try))
