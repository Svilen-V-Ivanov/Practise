class Controller:
    def __init__(self):
        self.players = list()
        self.supplies = list()

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player)

        return f"Successfully added: {', '.join(str(x.name) for x in added_players)}"

    def add_supply(self, *args):
        for item in args:
            self.supplies.append(item)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.get_player(player_name)

        if not player:
            return

        if sustenance_type not in ('Food', 'Drink'):
            return

        index, supply = self.get_supply(sustenance_type)
        if not supply and sustenance_type == 'Drink':
            raise Exception("There are no drink supplies left!")

        if not supply and sustenance_type == 'Food':
            raise Exception("There are no food supplies left!")

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        total_stamina = player.stamina + supply.energy
        if total_stamina > 100:
            player.stamina = 100
        else:
            player.stamina = total_stamina
        self.supplies.pop(index)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player(first_player_name)
        second_player = self.get_player(second_player_name)

        if first_player.stamina == 0 or second_player.stamina == 0:
            message = ''
            if first_player.stamina == 0:
                message += f"Player {first_player.name} does not have enough stamina.\n"
            if second_player.stamina == 0:
                message += f"Player {second_player.name} does not have enough stamina.\n"

            return message.strip()

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        second_player.stamina -= (first_player.stamina / 2)
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"

        first_player.stamina -= (second_player.stamina / 2)
        if first_player.stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, 'Drink')

    def __str__(self):
        message = ''
        for player in self.players:
            message += f"{str(player)}\n"

        for item in self.supplies:
            message += f"{item.details()}\n"

        return message.strip()

    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def get_supply(self, name):
        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == name:
                return index, supply

        return -1, None
