favourite_foods = ["pancakes", "chocolate", "macaroni cheese", "pizza"]

def replace_a_food(food_to_replace, new_food):
    favourite_foods[favourite_foods.index(food_to_replace)] = new_food
    return favourite_foods

print(replace_a_food("macaroni cheese", "spaghetti bolognese"))