import sys
from multiprocessing import Process, cpu_count
from time import time


def factorize_one_number(n: int):
    result_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            result_list.append(i)

    print(result_list)
    return result_list


def factorize(li: list):
    result_list = []
    for el in li:
        result_list.append(factorize_one_number(el))

    print(result_list)
    return result_list


if __name__ == "__main__":
    timer = time()
    print(factorize([10651060, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99887766]))
    print(f'Done by 1 process: {round(time() - timer, 4)}')  # ~ 19.7743 sec

    timer = time()
    prs = []

    print(f"cpu_count = {cpu_count()}")

    list_of_numbers = [10651060, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99887766]

    cpu_count = cpu_count()

    c = 0
    while c < len(list_of_numbers):

        for i in range(cpu_count):
            if (c + i) >= len(list_of_numbers):
                break

            pr = Process(
                target=factorize_one_number, args=(list_of_numbers[c + i],), daemon=True
            )  # daemon=True
            pr.start()
            prs.append(pr)

        c += cpu_count

    [el.join() for el in prs]
    print(f'Done by multiprocessing: {round(time() - timer, 4)}')  # ~ 6.5785 sec
    print("End program")
