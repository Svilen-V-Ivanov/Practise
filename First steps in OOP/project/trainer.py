from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        string = f"Pokemon Trainer {self.name}" + '\n'
        string += f"Pokemon count {len(self.pokemons)}" + '\n'

        for pokemon in self.pokemons:
            string += f"- {pokemon.pokemon_details()}" + '\n'

        return string.strip()
