#!/usr/bin/python3

import requests
import pandas as pd

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")
    pokemondf = pd.DataFrame(requests.get(f"{POKEURL}?limit=1000"))
    pokemondf.to_csv('~/mycode/pokemon/pokemon.csv')

if __name__ == "__main__":
    main()

