from flask import jsonify, abort, request
from flask_restful import Resource

from pokedex_extract import PokedexExtract


class Pokemon(Resource):

    def __init__(self):
        self.pokemons = []

    def abort_if_pokemon_doesnt_exist(self, name):
        if name not in self.pokemons:
            abort(404, message="Todo {} doesn't exist".format(name))

    def post(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        # TODO: check if the pokemon already exists
        name = request.json['name']
        pokedex_extract = PokedexExtract()
        pokedex_extract.get_pokemon_info(name)
        new_pokemon = pokedex_extract.pokemon
        self.pokemons.append(new_pokemon)

        return vars(new_pokemon), 201

    def get(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        name = request.json['name']
        print(self.pokemons)
        # for pokemon in self.pokemons:
        #     if pokemon.name == name:
        #         print(pokemon)
        #         return vars(pokemon), 200
        return {"pokemon": "not found"}, 404

    def put(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        name = request.json['name']

    def delete(self, name):
        pokemon = [pokemon for pokemon in self.pokemons if pokemon['name'] == name]
        if len(pokemon) == 0:
            abort(404)
        self.pokemons.remove(pokemon[0])
        return jsonify({'result': True})
