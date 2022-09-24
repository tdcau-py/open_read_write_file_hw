from pprint import pprint


def read_file(file: str) -> list:
    with open(file, encoding='utf-8') as file:
        recipes = file.read().split('\n')

    recipes_list = []
    while recipes:
        if '' in recipes:
            recipes_list.append(list(recipes[:recipes.index('')]))
            del recipes[0:recipes.index('') + 1]

        else:
            recipes_list.append(list(recipes[:]))
            recipes.clear()

    return recipes_list


def get_cook_book() -> dict:
    recipes_list = read_file('recipes.txt')
    recipes_book = {}

    for item in recipes_list:
        recipes_book[item[0]] = []

        for i in item[2:]:
            ingredients = i.split(' | ')
            recipes_book[item[0]].append({'ingredient_name': ingredients[0],
                                          'quantity': ingredients[1],
                                          'measure': ingredients[2]})

    return recipes_book


cook_book = get_cook_book()
pprint(cook_book)
