#atividade 2 listas
#contar maiores de idade
idades = [15, 22, 17, 35, 40, 13, 18]
maiorque18 = 0
for i in idades:
    if i >= 18:
        print(i)
        maiorque18=maiorque18+1
maiorque18=str(maiorque18)
print("existem: ",maiorque18,"maiores de idade")

#calcular média
total = 0
for i in idades:
    total=total+i
print("valor total das idades: ",total)
mediano = len(idades)
media=total/mediano
print("a média das idades é: ",media)

#contar quantos são menores
menorque18=0
for i in idades:
    if i <= 18:
        menorque18=menorque18+1
menorque18=str(menorque18)
print("existem ",menorque18," pessoas menores de idade")