#Imprima o modelo do carro.
#Altere o ano para 2020.
#Adicione um novo campo chamado "cor" com valor "prata".
#Remova a chave "modelo".
#Mostre todas as chaves e valores restantes.

carro = {"marca": "fiat", "modelo": "uno", "ano": "2010"}
print(carro["modelo"])

carro["ano"]="2020"

carro["cor"]="prata"

del carro ["modelo"]
print(carro)