def create_cook_book(file):
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            ingr_list = []
            for i in range(int(f.readline().strip())):
                value = f.readline().strip()
                split_value = value.split(' | ')
                ingr_dict = {'ingredient_name': split_value[0], 'quantity': int(split_value[1]), 'measure': split_value[2]}
                ingr_list.append(ingr_dict)
            f.readline()
            cook_book[dish] = ingr_list
    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    array_dish = {}
    for dish in dishes:
        try:
            array_dish[dish] += 1
        except KeyError:
            array_dish[dish] = 1
    ingredient_dict = {}
    for key, dish_values in array_dish.items():
        if create_cook_book('recipes.txt').get(key) != None:
            ingredient = create_cook_book('recipes.txt').get(key)
            for ingredients in ingredient:
                count_ingredients = ingredients['quantity'] * person_count * dish_values
                if ingredients['ingredient_name'] not in ingredient_dict:
                    ingredient_dict[ingredients['ingredient_name']] = {'measure' : ingredients['measure'],
                                                                        'quantity' : count_ingredients}
                else:
                    ingredient_dict[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                        'quantity': count_ingredients + count_ingredients}
    print(ingredient_dict)

get_shop_list_by_dishes(['Омлет', 'Омлет', 'Утка по-пекински', 'Утка по-пекински'], 10)










