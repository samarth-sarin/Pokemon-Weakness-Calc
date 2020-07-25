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
	both_weakness_list = []
	weakness_list = []
	extra_weakness_list = []

	weaknesses = soup.find("div", {"class": "dtm-weaknesses"})
	count = 1
	for poke_type in weaknesses.find_all('span'):
		if (poke_type.find("i", {"class": "extra-damage"})):
			extra_weakness_list.append(poke_type.text.strip())
			continue
		weakness_list.append(poke_type.text.strip())

	both_weakness_list.append(weakness_list)
	both_weakness_list.append(extra_weakness_list)
	return both_weakness_list

def format(pokemon, global_weakness_dict):
	soup = html_parse(pokemon)
	types = find_type(soup)
	both_weakness_list = find_weaknesses(soup)
	print(pokemon.capitalize())
	print("Type(s):")
	for poke_type in types:
		print(poke_type)
	print("\n")
	print("Weak to:")
	for weakness in both_weakness_list[0]:
		if (global_weakness_dict.get(weakness) == None):
			global_weakness_dict.update({weakness : 1})
		else:
			global_weakness_dict[weakness] += 1
		print(weakness)
	print("\n")
	if (len(both_weakness_list[1]) > 0):
		print("Very weak to:")
		for very_weak_type in both_weakness_list[1]:
			if (global_weakness_dict.get(very_weak_type) == None):
				global_weakness_dict.update({very_weak_type : 1.5})
			else:
				global_weakness_dict[very_weak_type] += 1
			print(very_weak_type)

	#print("\n")

def main():
	print("Pokemon Weakness Determiner")
	print("Enter the number of pokemon:")
	num_pokemon = int(input())
	pokedex = []
	weakness_dict = {}
	print("Please enter your Pokemon")
	for i in range(num_pokemon):
		pokemon = input()
		pokedex.append(pokemon.lower())

	print("\n")
	for pokemon in pokedex:
		format(pokemon, weakness_dict)
		print("\n")

	print("The pokemon you have entered are most weak to: ")

	global_weakness_sorted = sorted(weakness_dict.items(), key=lambda x: x[1], reverse=True)

	for i in global_weakness_sorted:
		print(i[0], i[1])


if __name__ == '__main__':
	main()