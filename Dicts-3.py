#Calcule o valor total em estoque (quantidade × preço de cada item).
#Mostre quais produtos têm menos de 5 unidades.
#Adicione um novo produto via input() com quantidade e preço.

estoque = {"Arroz": {"quantidade": 10, "preco": 5.99},"Feijão": {"quantidade": 7, "preco": 7.49}}
chaves=[]
total=0
for nome in estoque:
    chaves.append(nome)



for i in chaves:
    quantiaestocada=(estoque[i]["quantidade"])
    precototal=(estoque[i]["preco"])*quantiaestocada
    print("o valor do estoque do produto:",i,"é",precototal)

for i in chaves:
    quantiaestocada=(estoque[i]["quantidade"])
    if quantiaestocada < 5:
        print("o produto", i,"tem poucas unidades")

nomeitem=input("digite o nome do item a ser adicionado: ")
quantidadeitem=int(input("digite quantos do item devem ser adicionados: "))
precoitem=float(input("digite o preço do item: "))

estoque[nomeitem]={"quantidade":quantidadeitem, "preco": precoitem}
print(estoque)