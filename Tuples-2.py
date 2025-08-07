#Atividade 2 - Tuplas
#mostrar o produto mais caro
#média dos preços
#todos os nomes dos produtos sem preços
produtos = [("Arroz", 5.99), ("Feijão", 7.49), ("Macarrão", 4.29)]

precos=[]
for i in produtos:
    precos.append(i[1])
print(precos)

maiorpreco=precos.index(max(precos))
print("O maior preço é do produto:", produtos[maiorpreco][0])

total=sum(precos)
media=total/len(precos)
print("a média do valor dos produtos é",media)

for i in produtos:
    nome=i[0]
    print(nome)