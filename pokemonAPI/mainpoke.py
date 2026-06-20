import requests
import time

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None

name = input('Digite o nome do pokemon que deseja consultar: ').lower().strip()

print('Procurando...')
time.sleep(6)

print('Aguarde só mais um pouco')
time.sleep(5)

pokemon_info = get_pokemon_info(name)

if pokemon_info:
    print('Finalizando pesquisas')
    time.sleep(1)
    
    print(f"Nome: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Altura: {pokemon_info['height']}")
    print(f"Peso: {pokemon_info['weight']}")
    
else:
    print('Pokémon não encontrado')
    