# pokemon-api

### About

Uses BeautifulSoup to retrieve the info of Pokemon by name from 
https://www.pokemon.com/us/pokedex/


APIs to get pokemon info

http://0.0.0.0:5000/api/v1/pokemons/    
 
1. GET     
   Retrieves a pokemon by name  
   
   {
   "name" : "Bulbasaur"
   }
   

2. POST     
   Create a pokemon by name. Uses info from beautifulsoup extraction.
   
   {
   "name" : "Bulbasaur"
   }   


3. PUT     
   Retrieves a pokemon by name  
   
   {"name" : "Bulbasaur",
   
   "height" : "5.3",
   
   "weight": "15.0 lbs"
   }   
   

4. DELETE 
   Deletes a pokemon by name  
   
   {
   "name" : "Bulbasaur"
   }   


### Installation
1. Without docker
```
pip install -r requirements.txt
python3 api.py
```
2. Docker 
```
docker-compose up --build
```