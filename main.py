import requests
import json

URL = 'https://en.wikipedia.org/wiki/'

class CountryInfoFromWikipedia:

    JSON = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

    def get_country(self, cursor):
        self.cursor = cursor
        response = requests.get(f'{self.JSON}').json()
        self.size = len(response)
        country_name = response[self.cursor]['name']['common']
        return country_name

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        country = self.get_country(self.cursor)
        if self.cursor == self.size - 1:
            raise StopIteration
        return country

with open('country_link.json', 'w+', encoding='utf-8') as file:
    for country in CountryInfoFromWikipedia():
        wiki_link = {country: URL + country.replace(" ", "_")}
        json.dump(wiki_link, file, indent=2, ensure_ascii=False)


