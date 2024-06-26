from pathlib import Path
import argparse


""""условие: 
координаты - рациональные числа в диапазоне от 10 ** -38 до 10 ** 38  не выполняется для первых точек в примере
(0 меньше 10 ** -38)"""


def func_open(text_path: str) -> list:
    path = Path(text_path)
    with open(path, 'r', encoding='UTF-8') as file_date:
        return [num_str.strip() for num_str in file_date]


def func_circle(point_list: list, circle_list: list):
    for points in point_list[0:99]:
        if (10 ** -38) <= float(points.split(' ')[1]) <= (10 ** 38) and \
               (10 ** -38) <= float(points.split(' ')[0]) <= (10 ** 38):

            summ = (float(points.split(' ')[0]) - float(circle_list[0].split(' ')[0])) ** 2 + \
               (float(points.split(' ')[1]) - float(circle_list[0].split(' ')[1])) ** 2
            radius = float(circle_list[1]) ** 2

            if summ < radius:
                print('1\n')

            elif summ == radius:
                print('0\n')

            else:
                print('2\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='paths')

    parser.add_argument('arg_1', type=str)
    parser.add_argument('arg_2', type=str)

    arguments = parser.parse_args()

    func_circle(func_open(arguments.arg_2), func_open(arguments.arg_1))
