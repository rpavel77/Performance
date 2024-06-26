import argparse
from pathlib import Path


def func_open(text: str) -> list:
    path = Path(text)
    with open(path, 'r') as file:
        return list(map(int, [num_str.strip() for num_str in file]))


def func_decision(num_list: list):
    med_num = round(sum(num_list) // len(num_list))
    print(sum(abs(num - med_num) for num in num_list))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='files')
    parser.add_argument('file', type=str)
    arguments = parser.parse_args()

    func_decision(func_open(arguments.file))
