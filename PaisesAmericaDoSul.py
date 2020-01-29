from pylab import *
import pandas as pd

# Lê os dados do arquivo
dados = pd.read_csv('drinks.csv', sep =',', encoding ='cp1252')

# Variavel que armazena Países da América do Sul
argentina = dados.loc[dados['country'] == 'Argentina']
arg = list(argentina['country']), float(argentina['total_litres_of_pure_alcohol'])
bolivia = dados.loc[dados['country'] == 'Bolivia']
bol = list(bolivia['country']), float(bolivia['total_litres_of_pure_alcohol'])
brasil = dados.loc[dados['country'] == 'Brazil']
bra = list(brasil['country']), float(brasil['total_litres_of_pure_alcohol'])
chile = dados.loc[dados['country'] == 'Chile']
chi = list(chile['country']), float(chile['total_litres_of_pure_alcohol'])
colombia = dados.loc[dados['country'] == 'Colombia']
col = list(colombia['country']), float(colombia['total_litres_of_pure_alcohol'])
ecuador = dados.loc[dados['country'] == 'Ecuador']
ecu = list(ecuador['country']), float(ecuador['total_litres_of_pure_alcohol'])
paraguai = dados.loc[dados['country'] == 'Paraguay']
par = list(paraguai['country']), float(paraguai['total_litres_of_pure_alcohol'])
peru = dados.loc[dados['country'] == 'Peru']
per = list(peru['country']), float(peru['total_litres_of_pure_alcohol'])
uruguai = dados.loc[dados['country'] == 'Uruguay']
uru = list(uruguai['country']), float(uruguai['total_litres_of_pure_alcohol'])
venezuela = dados.loc[dados['country'] == 'Venezuela']
ven = list(venezuela['country']), float(venezuela['total_litres_of_pure_alcohol'])

# Lista com os Países
lista = [arg, bol, bra, chi, col, ecu, par, per, uru, ven]
# Lista que divide nome do País e Litros per capita
lista2 = [[], []]
for i, item in enumerate(lista):
    lista2[0].append(lista[i][0][0])
    lista2[1].append(lista[i][1])


def grafico():
    def autolabel(barra):
        for barra in barra:
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width() / 2., altura, '%.1f' % float(altura), ha='center', va='bottom')

    indice = np.arange(10)
    #Largura da barra.
    width = 0.4
    #Cria subplots.
    fig, ax = plt.subplots()
    #Cria a barra
    barra = ax.bar(indice, lista2[1], width, color='#DAA520', align='center')

    #Titulo do grafico.
    ax.set_title('Média do Consumo de Bebidas Alcoólicas (per capita)', size=15)
    #Posiciona o indice horizontal.
    ax.set_xticks(indice)
    #Indice horizontal.
    ax.set_xticklabels(lista2[0], rotation=30)

    #Insere as quantidades no topo das colunas.
    autolabel(barra)

    #Mostra o grafico.
    plt.show()


#Inicia o Programa e chamada a função gráfico
if __name__ == '__main__':
    grafico()
