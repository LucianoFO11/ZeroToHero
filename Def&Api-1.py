#peça ao usuario o nome de 3 criptomoedas
#use a função para pegar o preço de cada uma
#mostre os preços de forma organizada
import requests
listamoedas=[]
def pegarpreco(cripto):
    url=f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=brl"
    response=requests.get(url)
    dados=response.json()

    if cripto in dados:
        return dados[cripto]["brl"]
    else:
        print("deu errado")
        return None
for i in range(3):
    moeda = input("digite o nome da criptomoeda: ")
    valor=(pegarpreco(moeda))
    print(moeda," está por: R$", valor)
    precomoeda=(valor, moeda)
    listamoedas.append(precomoeda)

listamoedas.sort()
listamoedas.reverse()
for i in listamoedas:
    print(i[1], i[0])
