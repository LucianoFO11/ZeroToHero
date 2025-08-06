#atividade 1
listanomes = []
repetições=5
for i in range(repetições):
    newnome = input("Digite o nome: ")
    listanomes.append(newnome)
    print(listanomes)

listanomes.pop(2)
print(listanomes[0:2])
