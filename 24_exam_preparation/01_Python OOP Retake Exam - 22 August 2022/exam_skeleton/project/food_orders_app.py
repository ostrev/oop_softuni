import copy

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    valid_meals = ["Starter", "MainDish", "Dessert"]
    count = 0
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if any(c.phone_number == client_phone_number for c in self.clients_list):
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            meal_type = meal.__class__.__name__
            if meal_type in self.valid_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ''
        for meal in self.menu:
            result += meal.details()
            result += '\n'
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not any(c.phone_number == client_phone_number for c in self.clients_list):
            client = Client(client_phone_number)
            self.clients_list.append(client)
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        for meal, client_quantity in meal_names_and_quantities.items():
            if not any(m.name == meal for m in self.menu):
                raise Exception(f"{meal} is not on the menu!")
            if any(m.quantity < client_quantity for m in self.menu):
                meal_obj = [m for m in self.menu if m.name == meal][0]
                raise Exception(f"Not enough quantity of {meal_obj.__class__.__name__}: {meal}!")

        for meal, client_quantity in meal_names_and_quantities.items():
            for index in range(len(self.menu)):
                if self.menu[index].name == meal:
                    new_meal = copy.deepcopy(self.menu[index])
                    if not any(m.name == meal for m in client.shopping_cart):
                        new_meal.quantity = 0
                    new_meal.quantity += client_quantity
                    price_for_meal = client_quantity * self.menu[index].price
                    client.shopping_cart.append(new_meal)
                    client.bill += price_for_meal

                    self.menu[index].quantity -= client_quantity

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(m.name for m in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_c in client.shopping_cart:
            meal_from_menu = next(
                (obj for obj in self.menu if obj.name == meal_c.name),
                None
            )
            meal_from_menu.quantity += meal_c.quantity
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        self.count += 1

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        total = client.bill
        client.shopping_cart = []
        client.bill = 0
        return f"Receipt #{self.count} with total amount of {total:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


