estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
]
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50

# Em codigos mais complexos, iremos começar sempre do macro: top-down
# Para garantir que as fábricas vão ser impressas só uma vez, criaremos uma lista auxiliar:
fabricas_abaixo_nivel = []

for i, lista in enumerate(estoque):
    # Queremos saber se na lista tem alguém abaixo do nível mínimo, logo, analisaremos cada lista que está dentro da lista estoque e veremos se há algum número menor que 50
    for qtde in lista:
        if qtde < nivel_minimo:
            # print(qtde)
            # Agora, deveremos saber quais são as fábricas com esses números,  então precisamos saber o índice do primeiro for, que percorre a lista de estoque (retornar ao primeiro for e usar enumerate)
            # Ao invés de números são retornados os nomes das fábricas
            # print(fabricas[i])
            # Se a fábrica já estiver na lista de abaixo de nível, passar, se não, adicionar. Isso irá impedir repetições
            if fabricas[i] in fabricas_abaixo_nivel:
                pass
            else:
                fabricas_abaixo_nivel.append(fabricas[i])
# Mostra as fábricas que estão com estoque abaixo do mínimo
print(fabricas_abaixo_nivel)
