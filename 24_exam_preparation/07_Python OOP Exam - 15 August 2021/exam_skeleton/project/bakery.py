from project.helpers.drink_factory import DrinkFactory
from project.helpers.food_factory import FoodFactory
from project.helpers.table_factory import TableFactory


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = FoodFactory.create_food_by_type(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = DrinkFactory.create_drink_by_type(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(t.table_number == table_number for t in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = TableFactory.create_table_by_type(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        not_reserved_tables = [t for t in self.tables_repository if t.is_reserved is False]
        free_tables = [table for table in not_reserved_tables if table.capacity >= number_of_people]
        if not free_tables:
            return f"No available table for {number_of_people} people"
        else:
            table = free_tables[0]
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args: str):
        table_list = [t for t in self.tables_repository if t.table_number == table_number]
        if not table_list:
            return f"Could not find table {table_number}"
        table = table_list[0]
        result = f'Table {table_number} ordered:\n'
        result_not_in_menu = f'{self.name} does not have in the menu:\n'
        for food_name in args:
            food_list = [f for f in self.food_menu if f.name == food_name]
            if food_list:
                food = food_list[0]
                result += food.__repr__()
                result += '\n'
                table.order_food(food)
            else:
                result_not_in_menu += f'{food_name}\n'

        return result + result_not_in_menu.strip()

    def order_drink(self, table_number: int, *args: str):
        table_list = [t for t in self.tables_repository if t.table_number == table_number]
        if not table_list:
            return f"Could not find table {table_number}"
        table = table_list[0]
        result = f'Table {table_number} ordered:\n'
        result_not_in_menu = f'{self.name} does not have in the menu:\n'
        for drink_name in args:
            drink_list = [d for d in self.drinks_menu if d.name == drink_name]
            if drink_list:
                drink = drink_list[0]
                result += drink.__repr__()
                result += '\n'
                table.order_drink(drink)
            else:
                result_not_in_menu += f'{drink_name}\n'

        return result + result_not_in_menu.strip()

    def leave_table(self, table_number: int):
        table_list = [t for t in self.tables_repository if t.table_number == table_number]
        if not table_list:
            return f"Could not find table {table_number}"
        table = table_list[0]
        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        return f"Table: {table_number}\n" + \
            f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income}lv"

