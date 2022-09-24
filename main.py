from pprint import pprint
from typing import List
import os


def read_file(path_to_file: str) -> List[list]:
    """Читает данные из файла и группирует их в списки"""
    with open(path_to_file, encoding='utf-8') as file:
        recipes = file.read().split('\n')

    recipes_lists = []
    while recipes:
        if '' in recipes:
            recipes_lists.append(list(recipes[:recipes.index('')]))
            del recipes[0:recipes.index('') + 1]

        else:
            recipes_lists.append(list(recipes[:]))
            recipes.clear()

    return recipes_lists


def get_cook_book() -> dict:
    """Формирует словарь из сгруппированных данных"""
    file_name = 'recipes.txt'
    dir_path = os.getcwd()
    recipes_list = read_file(os.path.join(dir_path, file_name))
    recipes_book = {}

    for item in recipes_list:
        recipes_book[item[0]] = []

        for i in item[2:]:
            ingredients = i.split(' | ')
            recipes_book[item[0]].append({'ingredient_name': ingredients[0],
                                          'quantity': ingredients[1],
                                          'measure': ingredients[2]})

    return recipes_book


def get_shop_list_by_dishes(dishes: list, persons: int) -> dict:
    cook_book = get_cook_book()
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                shop_list[item['ingredient_name']] = {'measure': item['measure'],
                                                      'quantity': int(item['quantity']) * persons}

    return shop_list


new_shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(new_shop_list)
