import requests
import time
import sys

base_url = "https://pokeapi.co/api/v2/"


def menu():
    
    while True:
        
        print("\nBem-vindo a PokeAPI!")
        print("1 - Buscar Pokémon")
        print("2 - Ver histórico")
        print("3 - Sair")
        
        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print('Digite um valor válido')
            continue
        
        if escolha == 1:
            buscar_pokemon()
        elif escolha == 2:
            historico()
        elif escolha == 3:
            print('Obrigado por usar a PokeAPI!')
            print('Saindo...')
            sys.exit()
        
    

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    
    try:
        response = requests.get(url)
    
    except requests.exceptions.RequestException:
        print('Erro: Não foi possível conectar na API')
        return None
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None


def buscar_pokemon():
    
    name = input('Digite o nome do pokemon que deseja consultar: ').lower().strip()

    print('Procurando...')
    time.sleep(1)

    print('Aguarde só mais um pouco')
    time.sleep(0.5)

    pokemon_info = get_pokemon_info(name)

    if pokemon_info:
        print('Finalizando pesquisas')
        time.sleep(1)
                
        print(f"Nome: {pokemon_info['name'].capitalize()}")
        print(f"Id: {pokemon_info['id']}")
        print(f"Altura: {pokemon_info['height']}")
        print(f"Peso: {pokemon_info['weight']}")
        
        print("\nHabilidades: ")
                
        for habilidade in pokemon_info['abilities']:
            print(habilidade['ability']['name'].capitalize())
                    
        print("\nTipo: ")
                
        for tipo in pokemon_info['types']:
            print(tipo['type']['name'].capitalize())
        print('-'*30)
    else:
        print('Pokémon não encontrado')

def historico():
    print('Erro: Trabalhando nisso')


menu()