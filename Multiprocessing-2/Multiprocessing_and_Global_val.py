import multiprocessing

square_results = []


def calc_square(numbers):
    global square_results
    for num in numbers:
        print('square ' + str(num * num))
        square_results.append(num * num)
    print('Result within process ' + str(square_results))  # here square_results  list  - not empty


if __name__ == "__main__":
    arr = [2, 3, 6, 8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()

    print('Result ' + str(square_results))  # here we have had empty list  -  square_results IS global !!!!!
    print('Done!')
