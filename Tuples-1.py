#Tuples - Atividade 1
#print o primeiro e o ultimo valor
#contar quantos nomes tem na tupla
#verificar se um nome está na tupla
tuplaA = ("Arthur", "Isa", "Ricardo", "Pedro")

TuplaB = tuplaA[0::3]
print(TuplaB)

quantia=0
for i in tuplaA:
    quantia=quantia+1
print("a tupla tem",quantia,"nomes")



print("Digite o nome para verificar")
nome=input()
if nome in tuplaA:
    print("O nome está na tupla")
else:
    print("O Nome não está na tupla")