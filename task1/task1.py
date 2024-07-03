import numpy
from itertools import cycle
import argparse


""""Использую метод numpy.roll и передвигаю массив на себя с нужным шагом ,а не иду по нему c помощью cycle
(numpy быстрее)"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='paths')

    parser.add_argument('arg_1', type=int)
    parser.add_argument('arg_2', type=int)

    arguments = parser.parse_args()

    list_way = [1]
    cycle_mas = cycle([number for number in range(1, arguments.arg_1 + 1)])

    count = 1
    next_item = next(cycle_mas)

    while True:
        count += 1
        num = next(cycle_mas)

        if num == 1 and count % arguments.arg_2 == 0:
            break

        elif count == arguments.arg_2 and num != 1:
            count = 1
            list_way.append(num)

    print(''.join(list(map(str, list_way))))





""""метод numpy.roll и передвигая массив на себя с нужным шагом ,а не иду по нему c помощью cycle
(numpy быстрее)"""

   #  while True:
   #     overturn_list = numpy.roll(mass_list, shift=arguments.arg_1 - arguments.arg_2 + 1)

   #     list_way.append(overturn_list[0])
   #     mass_list = overturn_list
   #     if list_way[0] == overturn_list[arguments.arg_2 - 1]:
   #         break

   # print(''.join(list(map(str, list_way))))
