from graphql_api.pokemon_schema import schema


def query_pokemon():
    q1 = """
    {
      pokemon(name:"bulbasaur"){
      name
      height
      weight
      category
      abilities
      gender
      type
      weaknesses
      }
    }
    """
    q2 = """
    mutation createPokemon{
        createPokemon(name:"bulbasaur"){
            pokemon{
                name
                }
            }
        }
    """
    try:
        result = schema.execute(q2)
    except Exception as e:
        print(e)
        return []
    return result.data


if __name__ == "__main__":
    print(query_pokemon())
