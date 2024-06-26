import argparse
import json
from typing import Any
from pathlib import Path


"""Добавил indent для report.json для лучшей читабельности"""


def func_open(text_path: str) -> dict:
    path = Path(text_path)
    with open(path, 'r', encoding='UTF-8') as file_js:
        return json.load(file_js)


def func_close(dict_js, text_path):
    path = Path(text_path)
    with open(path, 'w') as file_out:
        json.dump(dict_js, file_out, indent=3)


def func_search_id(dict_data: Any, dict_values: dict, result=True) -> Any:
    count = False
    if isinstance(dict_data, list):
        for dict_tst in dict_data:
            if isinstance(dict_tst, dict):
                func_search_id(dict_tst, dict_values)
        return dict_data
    else:
        for keys, values in dict_data.items():
            if keys == "id":
                search_id = values
                result = func_search_value(search_id, dict_values)
                count = True
            elif count is True and keys == 'value':
                dict_data[keys] = result

            elif isinstance(values, list):
                func_search_id(values, dict_values)

        return dict_data


def func_search_value(search_id: int, dict_values: Any) -> str:
    count = False
    if isinstance(dict_values, list):
        for value_list in dict_values:
            if isinstance(value_list, dict):
                result = func_search_value(search_id, value_list)
                if result is not None:
                    return result
    else:
        for keys, values in dict_values.items():
            if isinstance(values, list):
                res = func_search_value(search_id, values)
                if res is not None:
                    return res
            elif keys == 'id' and values == search_id:
                count = True

            elif count is True and keys == 'value':
                return values


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='paths')

    parser.add_argument('path_values', type=str)
    parser.add_argument('path_tests', type=str)
    parser.add_argument('path_report', type=str)

    arguments = parser.parse_args()

    func_close(func_search_id(func_open(arguments.path_tests), func_open(arguments.path_values)), arguments.path_report)
