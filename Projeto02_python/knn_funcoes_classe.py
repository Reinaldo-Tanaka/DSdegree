class Modelando_knn():
    '''
    Esta classe possui métodos para classificar dados a partir do algoritmo KNN.
    Os argumentos pedidos são dados_treinados: que é uma coleção (em formato lista)
    já classificada - , dados_nao_treinados: são aqueles que gostaria-se de classi-
    ficar e valor_de_k - valor arbitrário normalmente ímpar.
    '''

    def __init__(self, dados_treinados, dados_nao_treinados, valor_de_k):
        self.dados_treinados = dados_treinados
        self.dados_nao_treinados = dados_nao_treinados
        self.valor_de_k = valor_de_k

    # Criando a função para distância (Etapa 3) - genérico!
    def calc_dist(self, dados_treinados, dados_nao_treinados):
        ''' Cálculo da distância euclidiana
        Vai se usar os valores dos investimentos (dentro da tupla) para calcular
        a distância entre o ponto desejado (não treinado) e o ponto já classificado
        (treinado).

        Entradas
        dados_treinados: dados dentro de uma lista, sendo que este mesmo dado será
        uma lista com CPF, classificação e uma tupla com os investimentos.
        Ex.:
        data = [[66707599984, 'Conservador', (5100., 3500., 1400., 200.)],
                 [55695397315, 'Conservador', (4900., 3000., 1400., 200.)],
                 [63743886918, 'Conservador', (4700., 3200., 1300., 200.)],
                 [55941368774, 'Conservador', (4600., 3100., 1500., 200.)]]

        dados_nao_treinados: similar aos dados_treinados, contudo, a classificação
        é uma string vazia.
        Ex.:
        no_class = [[45926320819, '', (5800., 4000., 1200., 200.)],
                     [52559670741, '', (5700., 4400., 1500., 400.)],
                     [59016004832, '', (5400., 3900., 1300., 400.)],
                     [66175672425, '', (5100., 3500., 1400., 300.)]]

        Saída
        distancia: tem-se uma variável: a distância do ponto. Sem unidade.
        '''
        lista_aux = list()
        for indice in range(0,len(dados_treinados[2])):
            lista_aux.append(dados_nao_treinados[2][indice] - dados_treinados[2][indice])
        for indice in range(len(lista_aux)):
            lista_aux[indice] = (lista_aux[indice] ** 2)
        distancia = (sum(lista_aux) ** (1/len(lista_aux)))
        return distancia

    # Para tirar os menores valores, vamos dar enumerate e criar uma nova lista
    # com as distâncias como primeiro item justamente para dar sort!!!!
    # Criando função para numerar a lista, deixar as menores distâncias no comecinho da lista,
    # e permanecendo apenas os "K" valores (Etapa 4)
    def manter_k_valores(self, lista_distancias):
        ''' Dentro de todas as distâncias calculadas, vai se manter as k primeiras
        Temos a lista com todas as distâncias e vai se utilizar as k mais
        próximas ao ponto desejado.

        Entrada
        lista_distancias: lista com os valores das distâncias

        Saída
        lista_numerada: será uma lista de tuplas as k menores distâncias e o
        índice dos dados treinados
        '''
        lista_numerada = list()
        for indice, distancia in enumerate(lista_distancias):
            lista_numerada.append([distancia, indice])
        lista_numerada.sort()
        lista_numerada = lista_numerada[:self.valor_de_k]
        return lista_numerada

    # Criando função para verificar a classificação do CPF (Etapa 5)
    def classificacao(self, lista_para_classificar):
        ''' Com as k classificações, determina-se qual categoria é maior
        Computou-se as menores distâncias e resgatou sua classificação, assim
        nesta função avalia-se numericamente qual rótulo tem maior quantidade

        Entrada
        lista_para_classificar: lista as k classificações

        Saída
        lista_base: uma string dentre as 3 classificações
        '''
        lista_base = [[0, 'Conservador'], [0, 'Moderado'], [0, 'Agressivo']]
        for identificacao in lista_para_classificar:
            if identificacao == 'Conservador':
                lista_base[0][0] = lista_base[0][0] + 1
            elif identificacao == 'Moderado':
                lista_base[1][0] = lista_base[1][0] + 1
            elif identificacao == 'Agressivo':
                lista_base[2][0] = lista_base[2][0] + 1
        lista_base.sort(reverse=True)
        return lista_base[0][1]
