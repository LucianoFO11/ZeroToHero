import requests
import tkinter as tk
from tkinter import messagebox

def pegarinfopoke(nomepokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nomepokemon.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Erro", f"Pokémon '{nomepokemon}' não encontrado!")
        return None

    dados = response.json()
    return {
        "nome": dados.get("name"),
        "peso": dados.get("weight") / 10,
        "altura": dados.get("height") / 10,
        "tipos": [t["type"]["name"] for t in dados.get("types")]
    }


def comparar():
    p1 = entry1.get()
    p2 = entry2.get()

    poke1 = pegarinfopoke(p1)
    poke2 = pegarinfopoke(p2)

    if poke1 and poke2:
        resultado = (
            f"{poke1['nome'].capitalize()} vs {poke2['nome'].capitalize()}\n\n"
            f"Peso: {poke1['peso']} kg   |   {poke2['peso']} kg\n"
            f"Altura: {poke1['altura']} m   |   {poke2['altura']} m\n"
            f"Tipos: {', '.join(poke1['tipos'])}   |   {', '.join(poke2['tipos'])}"
        )
        messagebox.showinfo("Comparação de Pokémon", resultado)


root = tk.Tk()
root.title("Comparação de Pokémon")

tk.Label(root, text="Nome do primeiro Pokémon:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nome do segundo Pokémon:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

botao = tk.Button(root, text="Comparar", command=comparar)
botao.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
