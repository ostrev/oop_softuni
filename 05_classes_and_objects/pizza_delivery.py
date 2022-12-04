class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False


    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += quantity * price_per_quantity
        else:
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.price -= quantity * price_per_quantity
        self.ingredients[ingredient] -= quantity

    def make_order(self):
        self.ordered = True
        result_list = []
        for k, v in self.ingredients.items():
            ingredient_string = f'{k}: {v}'
            result_list.append(ingredient_string)
        return f"You've ordered pizza {self.name} prepared with {', '.join(result_list)} and the price will be {self.price}lv."
