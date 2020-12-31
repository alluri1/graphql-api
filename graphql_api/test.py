from graphql_api.pokemon_schema import schema


def query_pokemon():
    q = """
    {
      website (url: "Bulbasaur" ) {
        name
        height
        weight
      }
    }
    """
    result = schema.execute(q)
    if result.errors:
        if len(result.errors) == 1:
            raise Exception(result.errors[0])
        else:
            raise Exception(result.errors)
    return result.data


if __name__ == "__main__":
    query_pokemon()
