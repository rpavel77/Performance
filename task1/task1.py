import numpy
import argparse


""""Использую метод numpy.roll и передвигаю массив на себя с нужным шагом ,а не иду по нему c помощью cycle
(numpy быстрее)"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='paths')

    parser.add_argument('arg_1', type=int)
    parser.add_argument('arg_2', type=int)

    arguments = parser.parse_args()
    mass_list = numpy.arange(1, arguments.arg_1 + 1)

    list_way = list()
    list_way.append(mass_list[0])

    while True:
        overturn_list = numpy.roll(mass_list, shift=arguments.arg_1 - arguments.arg_2 + 1)

        list_way.append(overturn_list[0])
        mass_list = overturn_list
        if list_way[0] == overturn_list[arguments.arg_2 - 1]:
            break

    print(''.join(list(map(str, list_way))))
