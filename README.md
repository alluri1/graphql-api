# pokemon-api

### About

- Uses BeautifulSoup to retrieve the info of Pokemon by name from 

   https://www.pokemon.com/us/pokedex/


-  GraphQL API's

   http://0.0.0.0:8000/api/v1/pokemons/


- REST APIs to get pokemon info

  http://0.0.0.0:5000/api/v1/pokemons/

   1. GET - Retrieves a pokemon by name
   
   2. POST - Create a pokemon by name. Uses info from beautifulsoup extraction.
   
   3. PUT  - Retrieves a pokemon by name. Can update height and weight of a pokemon by name
   
   4. DELETE    -   Deletes a pokemon by name

### Installation
1. GraphQL API - w/o docker
```
python3 graphql_api/server.py
```
2. REST API - w/o docker
```
pip install -r requirements.txt
python3 rest_api.py
```

3. Docker for REST API
```
docker-compose up --build
```