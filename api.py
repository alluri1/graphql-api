import flask
from flask_restful import Api

from resources.pokemon import Pokemon

app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


@app.route('/', methods=['GET'])
def hello():
    return "Hello! You can find pokemon info here"


api.add_resource(Pokemon, '/api/v1/pokemons/')

if __name__ == "__main__":
    app.run(debug=True)
