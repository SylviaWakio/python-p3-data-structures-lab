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
    # pass
    return [food["name"] for food in spicy_foods]


# This function takes a list of spicy foods and returns a list of names of each spicy food.
# It uses a list comprehension to iterate over the list of dictionaries and extract the "name" key from each dictionary.


def get_spiciest_foods(spicy_foods):
    # pass
    return [food for food in spicy_foods if food["heat_level"] > 5]


# This function takes a list of spicy foods and returns a list of dictionaries where the heat level is greater than 5.
# It uses a list comprehension with a conditional statement to filter the spicy foods based on the heat level.


# def print_spicy_foods(spicy_foods):
#     # pass
#     for food in spicy_foods:
#         heat_level = "🌶" * food["heat_level"]
#     print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")


# Example usage
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

print_spicy_foods(spicy_foods)


# This function takes a list of spicy foods and prints each spicy food in a specific format.
# It uses a for loop to iterate over the list of dictionaries and print the name, cuisine, and heat level.
# The heat level is represented by a string of "🌶" emojis, which is created by multiplying the "🌶" string with the heat level.


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # pass
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


# This function takes a list of spicy foods and a cuisine as input, and returns a single dictionary for the spicy food
# whose cuisine matches the input cuisine.
# It uses a for loop to iterate over the list of dictionaries and checks if the cuisine matches the input cuisine.
# When a match is found, it returns the corresponding dictionary and exits the function.


# def print_spiciest_foods(spicy_foods):
#     # pass
#     spiciest_foods = get_spiciest_foods(spicy_foods)
#     print_spicy_foods(spiciest_foods)


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food["heat_level"]
        if heat_level > 5:
            print(
                f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * heat_level}"
            )


# Example usage
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

print_spiciest_foods(spicy_foods)


# This function takes a list of spicy foods and prints only the spicy foods that have a heat level greater than 5.
# It first calls the get_spiciest_foods() function to get the list of spiciest foods.
# Then, it calls the print_spicy_foods() function to print the spiciest foods using the existing function we defined.


def get_average_heat_level(spicy_foods):
    # pass
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return int(average_heat_level)


# This function takes a list of spicy foods and calculates the average heat level.
# It uses a list comprehension to iterate over the list of dictionaries and sum up the heat levels.
# Then, it divides the sum by the number of spicy foods to calculate the average.
# Finally, it returns the average heat level as an integer value.


# def create_spicy_food(spicy_foods, spicy_food):
#     pass


def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods


class TestDataStructures:
    SPICY_FOODS = [
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


def test_create_spicy_food():
    new_spicy_foods = create_spicy_food(
        TestDataStructures.SPICY_FOODS,
        {
            "name": "Griot",
            "cuisine": "Haitian",
            "heat_level": 10,
        },
    )

    assert new_spicy_foods == [
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
        {
            "name": "Griot",
            "cuisine": "Haitian",
            "heat_level": 10,
        },
    ]


test_create_spicy_food()