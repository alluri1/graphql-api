# pokemon-api

### About

Uses BeautifulSoup to retrieve the info of Pokemon by name from 
https://www.pokemon.com/us/pokedex/


APIs to get pokemon info

http://127.0.0.1:5000/api/v1/pokemons/    
 
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
   
   {
   "name" : "Bulbasaur"
   }   
   

4. DELETE 
   Deletes a pokemon by name  
   
   {
   "name" : "Bulbasaur"
   }   


### Installation
```
pip install -r requirements.txt
python3 api.py
```