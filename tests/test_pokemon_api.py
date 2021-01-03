import requests


class TestPokemon:

    def test_index_page(self):
        url = 'http://0.0.0.0:5000'  # The root url of the flask app
        r = requests.get(url + '/')  # Assumses that it has a path of "/"
        assert r.status_code == 200  # Assumes that it will return a 200 response

    def test_get_pokemon(self):
        pass

    def test_put_pokemon(self):
        pass

    def test_delete_pokemon(self):
        pass

    def test_post_pokemon(self):
        pass
