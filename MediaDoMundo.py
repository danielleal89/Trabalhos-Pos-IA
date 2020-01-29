from pylab import *
import pandas as pd

# Lê os dados do arquivo
dados = pd.read_csv('drinks.csv', sep =',', encoding ='cp1252')
# Variavel que armazena os dados do Brasil
brasil = dados.loc[dados['country'] == 'Brazil']
# Lista somente com País e média
br = list(brasil['country']), float(brasil['total_litres_of_pure_alcohol'])
# Ordena em ordem crescente a quantidade
dados.sort_values(['total_litres_of_pure_alcohol'], inplace=True)

# Pega as ultimas 5 linhas, como os maiores consumidores
cincoMaiores = dados[188:]

# Armazena, País - Média por pessoa
lista = []
# Adiciona os Países a lista
lista.append(list(cincoMaiores['country']))
lista.append(list(cincoMaiores['total_litres_of_pure_alcohol']))
# Adiciona o Brasil a lista
lista[0].append(br[0][0])
lista[1].append(float(brasil['total_litres_of_pure_alcohol']))


def grafico():
    def autolabel(barra):
        for barra in barra:
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width() / 2., altura, '%.1f' % float(altura), ha='center', va='bottom')

    indice = np.arange(6)
    #Largura da barra.
    width = 0.4
    #Cria subplots.
    fig, ax = plt.subplots()
    #Cor das barras
    c = '#4682B4'
    #Cria a barra
    barra = ax.bar(indice, lista[1], width, color=(c, c, c, c, c, 'g'), align='center')

    #Titulo do grafico.
    ax.set_title('Países com Maior Consumo de Bebidas Alcoólicas', size=15)
    #Posiciona o indice horizontal.
    ax.set_xticks(indice)
    #Indice horizontal.
    ax.set_xticklabels(lista[0], rotation=30)
    #Indice Vertical
    ylabel('Litros por Pessoa', size=11)
    #Insere as quantidades no topo das colunas.
    autolabel(barra)

    #Mostra o grafico.
    plt.show()


#Inicia o Programa e chamada a função gráfico
if __name__ == '__main__':
    grafico()
