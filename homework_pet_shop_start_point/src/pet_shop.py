def get_pet_shop_name(input_shop):
    return input_shop["name"]

def get_total_cash(input_shop):
    return input_shop["admin"]["total_cash"]

def add_or_remove_cash(input_shop, cash_amount):
    input_shop["admin"]["total_cash"] += cash_amount

def get_pets_sold(input_shop):
    return input_shop["admin"]["pets_sold"]

def increase_pets_sold(input_shop, number_sold):
    input_shop["admin"]["pets_sold"] += number_sold

def get_stock_count(input_shop):
    return len(input_shop["pets"])

def get_pets_by_breed(input_shop, input_breed):
    pets_by_breed = []
    for pet in input_shop["pets"]:
        if pet["breed"] == input_breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(input_shop, input_name):
    pet_found = False
    for pet in input_shop["pets"]:
        if pet["name"] == input_name:
            pet_found = True
            return pet
    if pet_found == False:
        return None

def remove_pet_by_name(input_shop, input_name):
    pets_to_keep = []
    for pet in input_shop["pets"]:
        if pet["name"] != input_name:
            pets_to_keep.append(pet)
    input_shop["pets"] = pets_to_keep

def add_pet_to_stock(input_shop, input_new_pet):
    input_shop["pets"].append(input_new_pet)

def get_customer_cash(input_customer_index):
    return input_customer_index["cash"]

def remove_customer_cash(input_customer_index, cash_amount):
    input_customer_index["cash"] -= cash_amount

def get_customer_pet_count(input_customer_index):
    return len(input_customer_index["pets"])

def add_pet_to_customer(input_customer_index, input_new_pet):
    input_customer_index["pets"].append(input_new_pet)

def customer_can_afford_pet(input_customer_index, input_new_pet):
    if input_customer_index["cash"] >= input_new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(input_shop, input_pet, input_customer_index):
    if input_pet != None:
        if customer_can_afford_pet(input_customer_index, input_pet) == True:
            add_pet_to_customer(input_customer_index, input_pet)
            remove_customer_cash(input_customer_index, input_pet["price"])
            add_or_remove_cash(input_shop, input_pet["price"])
            increase_pets_sold(input_shop, 1)



