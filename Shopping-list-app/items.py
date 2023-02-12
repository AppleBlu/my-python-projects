items_dict = {"ketchup": {"category": "sauce", "ingredient": ["ketchup"]},
              "coke": {"category": "drink", "ingredient": ["coke"]},
              "hamburger": {"category": "meal", "ingredient": ["burger bun", "burger meat", "lettuce"]},
              "chicken nuggets": {"category": "meal", "ingredient": "chicken nuggets"}}

print(items_dict["ketchup"]["category"])

items_food_list = []
items_drink_list = []
items_sauce_list = []

for key, value in items_dict.items():
    if value["category"] == "meal":
        items_food_list.append(key)
    elif value["category"] == "drink":
        items_drink_list.append(key)
    elif value["category"] == "sauce":
        items_sauce_list.append(key)

print(items_food_list)
print(items_sauce_list)
print(items_drink_list)
print(items_dict.items())

