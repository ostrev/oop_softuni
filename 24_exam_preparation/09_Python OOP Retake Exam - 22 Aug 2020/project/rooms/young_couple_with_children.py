from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name, salary_one + salary_two, (len(children) + 2))

        self.room_cost = 30
        self.appliances = []
        self.children = children
        members_count = len(self.children) + 2
        for item in range(members_count):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())

        self.calculate_expenses(self.appliances, self.children)


