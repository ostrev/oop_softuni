class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        add_names = []
        for player in args:
            if player in self.players:
                continue
            self.players.append(player)
            add_names.append(player.name)
        return f"Successfully added: {', '.join(p for p in add_names)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def __find_player_by_name(self, player_name):
        return [p for p in self.players if p.name == player_name][0]

    # def __take_last_supply(self, supply_type: str):
    #     for i in range(len(self.supplies) - 1, 0, -1):
    #         if type(self.supplies[i]).__name__ == supply_type:
    #             return self.supplies.pop(i)
    #     if supply_type == "Food":
    #         raise Exception("There are no food supplies left!")
    #     if supply_type == "Drink":
    #         raise Exception("There are no drink supplies left!")

    # def sustain(self, player_name: str, sustenance_type: str):
    #     player = self.__find_player_by_name(player_name)
    #     if player.stamina == 100:
    #         return f"{player.name} have enough stamina."
    #     supply = self.__take_last_supply(sustenance_type)
    #     if supply:
    #         player._sustain_player(supply)
    #         return f"{player_name} sustained successfully with {supply.name}."

    def sustain(self, player_name: str, sustenance_type: str):
        if not any(p.name == player_name for p in self.players):
            return
        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        player = self.__find_player_by_name(player_name)

        if player.need_sustenance is False:
            return f"{player_name} have enough stamina."

        for s in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[s].__class__.__name__ == sustenance_type:
                supply = self.supplies.pop(s)
                break
        else:
            raise Exception(f"There are no {'drink' if sustenance_type == 'Drink' else 'food' } supplies left!")

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        result = ''
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)
        if first_player.stamina == 0:
            result += f"Player {first_player_name} does not have enough stamina.\n"
        if second_player.stamina == 0:
            result += f'Player {second_player.name} does not have enough stamina.\n'
        if result != '':
            return result.strip()

        if first_player.stamina < second_player.stamina:
            self.__attack(first_player, second_player)
            self.__attack(second_player, first_player)
        else:
            self.__attack(second_player, first_player)
            self.__attack(first_player, second_player)

        if first_player.stamina < second_player.stamina:
            return f"Winner: {second_player_name}"
        else:
            return f"Winner: {first_player_name}"

    @staticmethod
    def __attack(first_player, second_player):
        hit = first_player.stamina / 2
        if second_player.stamina - hit <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"
        else:
            second_player.stamina -= hit

    def next_day(self):
        for player in self.players:
            reduce = player.age * 2
            if player.stamina - reduce < 0:
                player.stamina = 0
            else:
                player.stamina -= reduce

        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = ''
        for p in self.players:
            result += str(p)
            result += '\n'
        for s in self.supplies:
            result += f"{s.details()}"
            result += '\n'
        return result.strip()
