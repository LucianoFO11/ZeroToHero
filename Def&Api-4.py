import requests
import tkinter as tk
from tkinter import ttk, messagebox

def pegarinfopoke(nomepokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nomepokemon.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    dados = response.json()
    pokemon = {
        "nome": dados.get("name"),
        "peso": dados.get("weight") / 10,
        "altura": dados.get("height") / 10,
        "tipos": [t["type"]["name"] for t in dados.get("types")]
    }
    return pokemon


def comparar():

    for row in tree.get_children():
        tree.delete(row)

    nome1 = entry1.get().strip()
    nome2 = entry2.get().strip()

    poke1 = pegarinfopoke(nome1)
    poke2 = pegarinfopoke(nome2)

    if not poke1 or not poke2:
        messagebox.showerror("Erro", "Um ou ambos os Pokémons não foram encontrados!")
        return

    atributos = ["Nome", "Peso (kg)", "Altura (m)", "Tipos"]

    for atributo in atributos:
        valor1 = poke1["nome"] if atributo == "Nome" else \
                 poke1["peso"] if atributo == "Peso (kg)" else \
                 poke1["altura"] if atributo == "Altura (m)" else \
                 ", ".join(poke1["tipos"])

        valor2 = poke2["nome"] if atributo == "Nome" else \
                 poke2["peso"] if atributo == "Peso (kg)" else \
                 poke2["altura"] if atributo == "Altura (m)" else \
                 ", ".join(poke2["tipos"])

        tree.insert("", "end", values=(atributo, valor1, valor2))



root = tk.Tk()
root.title("Comparador de Pokémons")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Pokémon 1:").grid(row=0, column=0, padx=5)
entry1 = tk.Entry(frame_inputs)
entry1.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Pokémon 2:").grid(row=0, column=2, padx=5)
entry2 = tk.Entry(frame_inputs)
entry2.grid(row=0, column=3, padx=5)

btn = tk.Button(frame_inputs, text="Comparar", command=comparar)
btn.grid(row=0, column=4, padx=10)


colunas = ("Atributo", "Pokemon 1", "Pokemon 2")
tree = ttk.Treeview(root, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

tree.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()
