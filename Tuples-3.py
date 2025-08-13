#calcular o valor total vendido por produto
#encontrar o produto mais vendido em valor
#ordenar as vendas por total
vendas = [
    ("Arroz", 10, 5.99),
    ("Feijão", 7, 7.49),
    ("Macarrão", 15, 4.29),
    ("Açúcar", 5, 3.89)
]
#calcular o valor total vendido por produto
vttp=[]
for i in vendas:
    nomeproduto=(i[0])
    precoproduto=(i[2])
    vendas=(i[1])
    vtvendas=precoproduto*vendas
    produtocomvalor=[vtvendas,nomeproduto]
    vttp.append(produtocomvalor)
    print("o produto",nomeproduto,"tem um total de",vtvendas,"em vendas")

#encontrar o produto mais vendido em valor
vttp.sort()
vttp.reverse()
print("o produto com o maior valor total vendido é:",vttp[0][1],"com",vttp[0][0], "em vendas")