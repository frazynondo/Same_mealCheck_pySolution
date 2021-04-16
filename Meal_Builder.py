from abc import ABC

from Same_meal_Check_PythonSolution.builder_interface import Int_Builder


class Meal_Builder(Int_Builder, ABC):

    def __init__(self, meal_name: str):
        self._meal = Meals()
        self._mealName = meal_name

    def get_mealName(self):
        return self._mealName

    def add_recipe(self, recipe):
        self._meal.recipes.append(recipe)
        return self

    def get_recipes(self):
        return self._meal.recipes

    def change_mealName(self, meal_name):
        self._mealName = meal_name
        return self

    # def __str__(self):
    #     return "Meal Name : {}  \nRecipes : {}".format(self._mealName, self.get_recipes())

    def CookMeal(self):
        meal_order = {self.get_mealName(): self.get_recipes()}
        return self


class Meals:

    def __init__(self):
        self.recipes = []


class MealOptions:
    @staticmethod
    def Build(meal_nam: str):
        return Meal_Builder(meal_nam)

    @staticmethod
    def same_meal_checker(meals):
        for i in meals:
            """Sort the meals first"""
            i.get_recipes().sort()

        result = ["SAME MEALS LIST"]
        for i in range(len(meals) - 1):
            j = i + 1
            count = 0
            for j in range(j, len(meals)):
                if meals[i].get_recipes() == meals[j].get_recipes():
                    count += 1
                    temp = " {} {} & {} are the same meals \n --> With recipes: {}" \
                        .format(str(count) + ".", meals[i].get_mealName(), meals[j].get_mealName(),
                                " - ".join(meals[i].get_recipes()))
                    result.append(temp)
        if result.__len__() > 1:
            return "\n".join(result)
        else:
            return "All meals are unique"


def RUN():
    Pizza = MealOptions.Build("Pizza") \
        .add_recipe("Pepperoni") \
        .add_recipe("Mushroom") \
        .add_recipe("Onions") \
        .add_recipe("Break") \
        .CookMeal()
    Stew_chicken = MealOptions.Build("Stew With Chicken") \
        .add_recipe("ground turmeric") \
        .add_recipe("onion") \
        .add_recipe("diced tomatoes") \
        .CookMeal()
    Jol = MealOptions.Build("Rice") \
        .add_recipe("Pepperoni") \
        .add_recipe("Mushroom") \
        .add_recipe("Onions") \
        .add_recipe("Break") \
        .CookMeal()
    T = MealOptions.Build("Test") \
        .add_recipe("Pepperoni") \
        .add_recipe("Mushroom") \
        .add_recipe("Onions") \
        .add_recipe("Break") \
        .CookMeal()
    ST = MealOptions.Build("ST Test") \
        .add_recipe("ground turmeric") \
        .add_recipe("onion") \
        .add_recipe("diced tomatoes") \
        .CookMeal()
    Meal_list = [Pizza, Stew_chicken, Jol, T, ST]

    Test = MealOptions.same_meal_checker(Meal_list)
    print(Test)


RUN()
