import requests

def pegarinfopoke(nomepokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nomepokemon.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Pokémon não encontrado!")
        return

    dados = response.json()

    print("Nome:", dados.get("name"))
    print("Peso:", dados.get("weight") / 10, "kg")
    print("Altura:", dados.get("height") / 10, "m")

    tipos = dados.get("types")
    tipos_nomes = [t["type"]["name"] for t in tipos]
    print("Tipos:", ", ".join(tipos_nomes))

pegarinfopoke(input("Digite o nome do Pokémon: "))
