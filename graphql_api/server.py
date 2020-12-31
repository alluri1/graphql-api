"""
Python HTTP server for GraphQL.
"""
from flask import Flask
from flask_graphql import GraphQLView
from graphql_api.pokemon_schema import schema


app = Flask(__name__)
app.add_url_rule('pokemons/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.run()