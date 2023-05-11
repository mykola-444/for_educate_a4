import os


# function without arguments
# def create_folder():
#    os.mkdir("D:\\Tesingworld")
# def create_sub_folder():
#    os.mkdir("D:\\Tesingworld\\Urkaine")

# function with arguments
def create_folder(foldername):
    os.mkdir("D:\\" + foldername)


def create_sub_folder(subfoldername):
    os.mkdir("D:\\Tesingworld\\" + subfoldername)


# function with arguments and return value as well
def concatenate_two_values(val1, val2):
    val3 = val1 + "  " + val2
    return val3
