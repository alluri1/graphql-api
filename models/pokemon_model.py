class PokemonModel:

    def __init__(self, name=None, weight=None, height=None, gender=None,
                 category=None, abilities=None, type=None, weaknesses=None):
        self.name = name
        self.weight = weight
        self.height = height
        self.category = category
        self.abilities = abilities
        self.gender = gender
        self.type = type
        self.weaknesses = weaknesses

    def __repr__(self):
        return f'Pokemon(name = {self.name}, ' \
               f'weight = {self.weight}, ' \
               f'height = {self.height}, ' \
               f'category = {self.category}, ' \
               f'abilities = {self.height}, ' \
               f'gender = {self.gender}, ' \
               f'type = {self.type}, ' \
               f'weaknesses = {self.weaknesses})'


if __name__ == "__main__":
    pokemon = PokemonModel(name="Bulbasaur", weight="28.7 lbs")
    print(pokemon)
