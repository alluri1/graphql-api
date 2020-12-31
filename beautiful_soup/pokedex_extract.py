import os
import urllib.request

import requests
from bs4 import BeautifulSoup

from models.pokemon_model import PokemonModel


class PokedexExtract:

    def __init__(self):
        self.attributes = {}
        self.pokemon = PokemonModel()

    def get_pokemon_info(self, pokemon_name):
        URL = 'https://www.pokemon.com/us/pokedex/' + pokemon_name
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser').body

        # set the name of pokemon
        self.pokemon.name = pokemon_name

        # get required info from the soup object
        self.get_physical_attributes(soup)
        self.get_pokemon_type(soup)
        self.get_pokemon_weaknesses(soup)
        self.get_pokemon_image(soup, pokemon_name)

    def get_physical_attributes(self, soup):
        left_info_elements = soup.find('div', class_='column-7').find_all("li")
        right_info_elements = soup.find('div', class_='column-7 push-7').find_all("li")
        left_info_elements.extend(right_info_elements)

        for element in left_info_elements:
            try:
                title = element.find("span", class_="attribute-title").string
                if title == "Gender":
                    gender_icon_elements = element.find("span", class_="attribute-value").find_all("i")
                    value = [x.get("class")[1].split("_")[1] for x in gender_icon_elements]
                    self.pokemon.gender = value
                else:
                    value = element.find("span", class_="attribute-value").string

                if title == "Weight":
                    self.pokemon.weight = value
                elif title == "Height":
                    self.pokemon.height = value
                elif title == "Category":
                    self.pokemon.category = value
                elif title == "Abilities":
                    # TODO: fix abilities in pokemon object
                    print("abilities: ", value)
                    self.pokemon.abilities = value
                self.attributes[title] = value

            except AttributeError as ae:
                print(ae)

    def get_pokemon_type(self, soup):
        dtm_type_element = soup.find('div', class_="dtm-type")
        types_element = dtm_type_element.find_all("li")
        types = [element.a.string for element in types_element]
        self.attributes["Type"] = types
        self.pokemon.type = types

    def get_pokemon_weaknesses(self, soup):
        weaknesses_elements = soup.find('div', class_="dtm-weaknesses").find_all("li")
        weaknesses = [element.a.span.string.strip() for element in weaknesses_elements]
        self.attributes["Weaknesses"] = weaknesses
        self.pokemon.weaknesses = weaknesses

    def get_pokemon_image(self, soup, pokemon_name):
        images_directory = os.listdir("images/")
        if pokemon_name + ".jpg" not in images_directory:
            images_element = soup.find("div", class_="profile-images").find("img")
            image_url = images_element.attrs.get("src")
            urllib.request.urlretrieve(image_url, os.path.join("images/", pokemon_name + ".jpg"))


if __name__ == "__main__":
    pokedex_extract = PokedexExtract()
    pokedex_extract.get_pokemon_info("ivysaur")
    attributes = pokedex_extract.attributes
    print(attributes)
    pokemon_obj = pokedex_extract.pokemon
    print(pokemon_obj)
