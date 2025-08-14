#criar uma função para escolher uma atividade com o tipo fornecido
#pergunte ao usuario se ele quer filtrar por tipo ou aleatório
import requests
import random

def atividaderandom():
    urlrandom=f"https://bored-api.appbrewery.com/random"
    response=requests.get(urlrandom)
    dados=response.json()
    print("atividade:",dados.get("activity"))
    print("disponibilidade:",dados.get("availability"))
    print("tipo:",dados.get("type"))
    print("participantes:",dados.get("participants"))
    print("preço:",dados.get("price"))
    print("acessibilidade:",dados.get("accessibility"))


def choiceatividade(tipoatividade):
    urlchoice=f"https://bored-api.appbrewery.com/filter?type={tipoatividade}"
    response=requests.get(urlchoice)
    dados=response.json()
    atividadeescolhida=random.choice(dados)
    print("atividade:",atividadeescolhida["activity"])
    print("disponibilidade:",atividadeescolhida["availability"])
    print("tipo:",atividadeescolhida["type"])
    print("participantes:",atividadeescolhida["participants"])
    print("preço:",atividadeescolhida["price"])
    print("acessibilidade:",atividadeescolhida["accessibility"])
    print("link:",atividadeescolhida["link"])

print('_____________')
print('1- educação')
print('2- recreacional')
print('3- social')
print('4- caridade')
print('5- cozinha')
print('6- relaxamento')
print('7- trabalhoso')
print('8- aleatório')
print('_____________')
tipoatividade=""
escolha=int(input("Digite a opção desejada: "))


if escolha==1:
    tipoatividade="education"
    choiceatividade(tipoatividade)
elif escolha==2:
    tipoatividade="recreational"
    choiceatividade(tipoatividade)
elif escolha==3:
    tipoatividade="social"
    choiceatividade(tipoatividade)
elif escolha==4:
    tipoatividade="charity"
    choiceatividade(tipoatividade)
elif escolha==5:
    tipoatividade="cooking"
    choiceatividade(tipoatividade)
elif escolha==6:
    tipoatividade="relaxation"
    choiceatividade(tipoatividade)
elif escolha==7:
    tipoatividade="busywork"
    choiceatividade(tipoatividade)
elif escolha==8:
    atividaderandom()
else:
    print("escolha inválida")