from src.models.ingredient import Ingredient
from src.models.dish import Dish
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = self.read_file()

    def read_file(self):
        file = pd.read_csv(self.path)
        update_dishes = set()
        for _, dish, price, ingredient, recipe_amount in file.itertuples():
            dish = Dish(dish, price)
            ingredient = Ingredient(ingredient)
            dish.add_ingredient_dependency(ingredient, recipe_amount)

            if dish not in update_dishes:
                update_dishes.add(dish)
            else:
                for old_dish in update_dishes:
                    if old_dish == dish:
                        old_dish.add_ingredient_dependency(
                            ingredient, recipe_amount)
        return update_dishes
