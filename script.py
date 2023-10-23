from welcome import welcome
from linkedlist import LinkedList
from data import types, restaurant_data
import sys

welcome()
def insert_food_types():
    food_types = LinkedList()
    for type in types:
        food_types.insert_beginning(type)
    return food_types

def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_type in types:
        restaurant_data_sub_list = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == food_type:
                restaurant_data_sub_list.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_data_sub_list)
    return restaurant_data_list

food_types = insert_food_types()
restaurant_data = insert_restaurant_data()

print(restaurant_data.get_head_node().get_value().get_head_node().get_value())
print(food_types.get_head_node().get_value())

while True:
    while True:
        print("Enter the first few letters of the type of food you want...")
        food_type_str = input("> ").lower()

        match_food_type = []
        for type in types:
            if type.startswith(food_type_str):
                match_food_type.append(type)

        if not match_food_type:
            print("There is no food type in our inventory that contain the letters you entered. \n"
                  "Do you want to try entering the first few letters of a different type of food? (y / n)")
            try_diff_type_food = input("> ").lower()
            if try_diff_type_food == "n":
                sys.exit()
            else:
                pass
        else:
            food_type_selected = ""
            print(match_food_type)
            if len(match_food_type) == 1:
                print("There is only one food type that matches the letters you entered. Do you want to continue searching "
                      "other food types? (y / n)")
                search_other_food_types = input("> ").lower()
                if search_other_food_types == "y":
                    pass
                else:
                    food_type_selected = str(match_food_type[0])
                    break
            else:
                print("Of the options listed, which food type do you want to get a list of restaurants for? \n"
                      "Type the list of letters of the food type you want.")
                restaurants_to_display = input("> ").lower()
                for index, food_type in enumerate(match_food_type):
                    if food_type.startswith(restaurants_to_display):
                        food_type_selected = str(match_food_type[index])
                        break
                break

    print(f"Restaurants for {food_type_selected.title()}:")
    restaurant_string = restaurant_data.get_head_node()
    while restaurant_string.get_value() is not None:
        sub_restaurant_string = restaurant_string.get_value().get_head_node()
        if sub_restaurant_string.get_value()[0] == food_type_selected:
            while sub_restaurant_string.get_value() is not None:
                print(f"Restaurant Name: {sub_restaurant_string.get_value()[1]}")
                print(f"Prices: {sub_restaurant_string.get_value()[2]}/5")
                print(f"Rating: {sub_restaurant_string.get_value()[3]}/5")
                print(f"Address: {sub_restaurant_string.get_value()[4]}")
                print("-----------------------------------------")
                sub_restaurant_string = sub_restaurant_string.get_link_node()
            break
        else:
            restaurant_string = restaurant_string.get_link_node()

    continue_search = input("Do you want to search for a different food type? (y / n) >").lower()
    if continue_search == "n":
        sys.exit()
































