from multiprocessing import Process
import os


def square_numbers():
    for i in range(100):
        i * i


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()  # number of CPU on the current machine
    print("___________________NUM", num_processes)

    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    for process in processes:  # start all processes
        process.start()

    for process in processes:  # wait for all processes to finish
        process.join()  # block the main programme until all processes are finished
