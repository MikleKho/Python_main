# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import itertools

items_dict = {  "плащ": 0.5, 
                "палатка": 7, 
                "горелка": 1.5, 
                "посуда": 1.5, 
                "инструмент": 4, 
                "спальник": 1,
                "консервы": 2,
                "крупы": 4,
                "фонарь": 0.5,
                "чистая вода": 3}
WEIGHT_LIMIT = 15.0
weight_total = sum(items_dict.values())
amount_in_pack = len(items_dict)
variants_for_pack = [{None: None}]
flag_something_good = True

while flag_something_good == True:
    flag_something_good = False
    if len(variants_for_pack) > 1 and variants_for_pack[0] == {None: None}:
        variants_for_pack.pop(0)

    for item_pack_maybe in itertools.combinations(items_dict.items(), amount_in_pack):
        flag_adding = False

        if (sum(dict(item_pack_maybe).values())) > WEIGHT_LIMIT:
            flag_something_good = True
            continue
        else:
            flag_adding = False

            for variant_for_pack in variants_for_pack:

                if set(variant_for_pack).issuperset(set(item_pack_maybe)):
                    flag_adding = False
                    break
                else:
                    flag_adding = True
                    flag_something_good = True

            if flag_adding:
                variants_for_pack.append(set(item_pack_maybe))

    amount_in_pack -= 1
    if amount_in_pack == 0:
        flag_something_good = False

print('             ---------------------          ')
print('Общий список: ', items_dict )
print('             ---------------------          ')
print('В рюкзак помещаются следующие наборы:')
for i in variants_for_pack:
    print('---------------------')
    print(i)
