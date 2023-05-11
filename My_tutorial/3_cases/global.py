command = "You are a LOVELY person!"


def shout():
    global command
    print("in func= ", command)
    command = "You are amazing!!"


shout()
print("out fanc= ", command)
