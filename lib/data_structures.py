spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # for food in spicy_foods:
    #     return [value for key, value in food if key == "name"] 
    return [value for food in spicy_foods for key, value in food.items() if key == "name"]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get("cuisine")
        level = "🌶" * food.get("heat_level")
        print(f"{name} ({cuisine}) | Heat Level: {level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    spicy = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy)
    pass

def get_average_heat_level(spicy_foods):
    # total = 0
    # for food in spicy_foods:
    #     total += food.get("heat_level")
    # return total / len(spicy_foods)

    heat_levels = [food.get("heat_level") for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    # append modifies in palce and returns None
    # need to append first then return
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
