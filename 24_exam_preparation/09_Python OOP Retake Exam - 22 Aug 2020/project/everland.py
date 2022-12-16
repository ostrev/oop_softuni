from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
            total_consumption += room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            if room.budget >= (room.expenses + room.room_cost):
                room.budget -= (room.expenses + room.room_cost)
                result += f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return result.strip()

    def status(self):
        result = ''
        total_people_in_hotel = 0
        children_total = 0
        count = 0
        for room in self.rooms:
            total_people_in_hotel += room.members_count
        result += f'Total population: {total_people_in_hotel}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if room.children:
                for child in room.children:
                    count += 1
                    children_total += child.get_monthly_expense()
                    result += f'--- Child {count} monthly cost: {child.get_monthly_expense():.2f}$\n'
                count = 0

            result += f'--- Appliances monthly cost: {(room.expenses - children_total):.2f}$\n'
            children_total = 0

        return result.strip()