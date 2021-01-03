from graphene import Mutation, String, List, ObjectType, Field, Schema

from beautiful_soup.pokedex_extract import PokedexExtract


class Pokemon(ObjectType):
    name = String()
    weight = String()
    height = String()
    category = String()
    abilities = String()
    gender = List(String)
    type = List(String)
    weaknesses = List(String)


class CreatePokemon(Mutation):
    class Arguments:
        name = String()

    pokemon = Field(Pokemon)

    def mutate(self, info, name):
        pokedex_extract = PokedexExtract()
        pokedex_extract.get_pokemon_info(name)
        new_pokemon = pokedex_extract.pokemon

        return CreatePokemon(new_pokemon)


class Mutation(ObjectType):
    create_pokemon = CreatePokemon.Field()


class Query(ObjectType):
    pokemon = Field(Pokemon, name=String())

    def resolve_pokemon(self, info, name):
        pokedex_extract = PokedexExtract()
        pokedex_extract.get_pokemon_info(name)
        new_pokemon = pokedex_extract.pokemon
        return Pokemon(name=name,
                       weight=new_pokemon.weight,
                       height=new_pokemon.height,
                       category=new_pokemon.category,
                       abilities=new_pokemon.abilities,
                       gender=new_pokemon.gender,
                       type=new_pokemon.type,
                       weaknesses=new_pokemon.weaknesses
                       )


schema = Schema(query=Query, mutation=Mutation)
