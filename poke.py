import requests
from bs4 import BeautifulSoup

def html_parse(pokemon):
	url = 'https://www.pokemon.com/us/pokedex/' + pokemon
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text, 'html.parser')
	return soup

def find_type(soup):
	types_list = []
	types = soup.find("div", {"class": "dtm-type"})
	for poke_type in types.find_all('a'):
		types_list.append(poke_type.text.strip())
	return types_list

def find_weaknesses(soup):
	weakness_list = []
	weaknesses = soup.find("div", {"class": "dtm-weaknesses"})
	for poke_type in weaknesses.find_all('span'):
		weakness_list.append(poke_type.text.strip())
	return weakness_list

def format(pokemon):
	soup = html_parse(pokemon)
	types = find_type(soup)
	weaknesses = find_weaknesses(soup)
	print(pokemon.capitalize())

	print("Type(s):")
	for poke_type in types:
		print(poke_type)
	print("\n")

	print("Weak to:")
	for weakness in weaknesses:
		print(weakness)
	print("\n")


def main():
	print("Pokemon Weakness Determiner")
	print("Enter the number of pokemon:")
	num_pokemon = int(input())
	pokedex = []

	for i in range(num_pokemon):
		pokemon = input()
		pokedex.append(pokemon.lower())

	print("\n")
	for pokemon in pokedex:
		format(pokemon)
		print("\n")


if __name__ == '__main__':
	main()