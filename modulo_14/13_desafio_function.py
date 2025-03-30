'''#exemplo mais simples para facilitar a visualização
precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147]

# Vamos definir qual o fator que vamos dividir as listas (ou seja, quantos % da lista vai ficar pra teste. O resto fica pra treino)
#Vamos usar 0.1 (10%)
fator = 0.1

#Isso significa que a lista de teste tem quantos itens? Através da variável i, iremos verificar quantos itens teremos na lista de testes
# Vai dar 9
i = int((1 - fator) * len(precos_imoveis))

#Agora vamos entender qual conta temos que fazer para dividir a lista em 2 listas. Uma com 90% dos valores e outra com 10%

# Lista de teste irá pegar todos os itens até o i, mas sem pegar o i
precos_teste = precos_imoveis[i:]

# Lista de treino irá pegar todos os itens a partir do i, mas incluindo o i
precos_treino = precos_imoveis[:i]

print(precos_teste)
print(precos_treino)'''

precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37,2.4,1.72,2,1.69,1.63,2.01,2.25,1.61,1.02,1.19,1.86,2.15,2.03,1.61,1.52,1.56,1.69,1.47,1.09,2.47,1.62,2.15,1.81,2.49,2.08,1.02,1.68,1.53,1.2,1.29,1.88,1.92,2.14,1.95,2.48,2.44,1.41,1.98,1.89,1.69,1.95,1.42,1.57,2.32,1.23,1.43,1.35,1.49,2.39,2.37,1.3,2.25,1.5,1.35,2.06,1.05,1.7,2.29,2.44,2.09,1.81,2.04,2.45,1.42,2.09,2.19,2.09,1,2.23,1.39,2,1.29,1.55,1.67,2.06,1.89,2.07,2.39,1.93,1.51,1.73,1.66,1.18,1.13,1.69,2.48,1.26,1.75, 1.51, 1.73]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147,222,165,184,175,147,217,214,171,86,111,180,211,210,168,156,154,179,163,99,246,162,205,195,263,198,121,149,140,122,119,197,210,218,202,258,256,135,203,173,152,197,145,154,252,141,141,151,133,232,229,134,215,155,138,186,120,152,213,256,219,200,210,238,140,224,233,222,120,233,151,185,111,149,186,194,194,222,223,185,157,154,164,129,128,169,240,136,191, 157, 154]

# O fator deve ficar como parâmetro, pois ele será o separador
# Importante: devemos fazer as comparações e operações com os parâmetros, e não com as listas de fora

def separar_listas(precos, tamanhos, fator = 0.1):
    # As listas devem possuir o mesmo tamanho
    if len(precos) == len(tamanhos):
        i_precos = int((1 - fator) * len(precos))
        i_tamanhos = int((1 - fator) * len(tamanhos))
        precos_teste = precos[i_precos:]
        precos_treino = precos[:i_precos]
        tamanhos_teste = tamanhos[i_tamanhos]
        tamanhos_treino = tamanhos[:i_tamanhos]
        return precos_teste, precos_treino, tamanhos_teste, tamanhos_treino
    else:
        print("As listas de preços e tamanhos dos imóveis não têm o mesmo tamanho")
        # Para a função terminar
        return

precos_teste, precos_treino, tamanhos_teste, tamanhos_treino = separar_listas(precos_imoveis, tamanho_imoveis)

# Imprimir a lista desejada
print(precos_teste)

