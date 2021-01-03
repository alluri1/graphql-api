"""
Python Flask server for GraphQL
"""
from flask import Flask
from flask_graphql import GraphQLView

from graphql_api.pokemon_schema import schema

app = Flask(__name__)
app.add_url_rule('/api/v1/pokemons/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.run(host="0.0.0.0", debug=True, port=8000)
