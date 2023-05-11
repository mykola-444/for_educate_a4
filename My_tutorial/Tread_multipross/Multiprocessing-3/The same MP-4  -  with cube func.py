# https://www.youtube.com/watch?v=fKl2JW_qrso
import concurrent.futures

calc_rez = []


def calc_cube(numbers):
    global calc_rez
    for num in numbers:
        print('cube ' + str(num * num * num))
        calc_rez.append(num * num * num)
    return 'Result within process ' + str(calc_rez)


if __name__ == "__main__":

    with concurrent.futures.ProcessPoolExecutor() as executor:
        numbers = [5, 4, 3, 2]
        result = [executor.submit(calc_cube, numbers)]

        for f in concurrent.futures.as_completed(result):  # as_completed method - return result
            print(f.result())

    print('Result ' + str(calc_cube))
    print('Done!')
