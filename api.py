import flask
from flask import jsonify, abort, request
from flask_restful import Api

from pokedex_extract import PokedexExtract

app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)
pokemons = []


@app.route('/', methods=['GET'])
def hello():
    return "Hello! You can find pokemon info here"


@app.route('/api/v1/pokemons/', methods=['POST'])
def create_pokemon():
    if not request.json or not 'name' in request.json:
        abort(400)
    # TODO: check if the pokemon already exists
    name = request.json['name']
    pokedex_extract = PokedexExtract()
    pokedex_extract.get_pokemon_info(name)
    new_pokemon = pokedex_extract.pokemon
    pokemons.append(new_pokemon)

    return vars(new_pokemon), 201


@app.route('/api/v1/pokemons/', methods=['GET'])
def get_pokemon():
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    print(pokemons)
    for pokemon in pokemons:
        if pokemon.name == name:
            return vars(pokemon)
    return {"pokemon": "not found"}, 404


@app.route('/api/v1/pokemons/', methods=['PUT'])
def put_pokemon():
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    height = request.json["height"]
    weight = request.json['weight']
    for pokemon in pokemons:
        if pokemon.name == name:
            pokemon.height = height
            pokemon.weight = weight
            return vars(pokemon)
    abort(404)


@app.route('/api/v1/pokemons/', methods=['DELETE'])
def delete_pokemon():
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    for idx, pokemon in enumerate(pokemons):
        if pokemon.name == name:
            pokemons.remove(pokemon)
            return jsonify({'result': True})
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
