estoque_fim_jan = [('BSA2199',396),('PPF5239',251),('BSA1212',989),('PPF2154',449),('BEB3410',241),('PPF8999',527),('EMB9591',601),('BSA2006',314),('EMB3604',469),('EMB2070',733),('PPF9018',339),('PPF1468',906),('BSA5819',291),('PPF8666',850),('BEB2983',353),('BEB5877',456),('PPF5008',963),('PPF3877',185),('PPF7321',163),('BSA8833',644),('PPF4980',421),('PPF3063',757),('BSA2089',271),('BSA8398',180),('EMB4622',515),('EMB9814',563),('PPF3784',229),('PPF2398',270),('BEB3211',181),('PPF8655',459),('PPF1874',799),('PPF8789',126),('PPF6324',375),('EMB9290',883),('BSA5516',555),('BSA8451',243),('BSA8213',423)]
estoque_fim_fev = [('BSA2199',849),('PPF5239',877),('BSA1212',336),('PPF2154',714),('BEB3410',834),('PPF8999',201),('EMB9591',576),('BSA2006',985),('EMB3604',615),('EMB2070',182),('PPF9018',127),('PPF1468',212),('BSA5819',338),('PPF8666',751),('BEB2983',363),('BEB5877',916),('PPF5008',331),('PPF3877',744),('PPF7321',488),('BSA8833',277),('PPF4980',530),('PPF3063',796),('BSA2089',396),('BSA8398',478),('EMB4622',603),('EMB9814',784),('PPF3784',434),('PPF2398',896),('BEB3211',826),('PPF8655',748),('PPF1874',210),('PPF8789',891),('PPF6324',250),('EMB6618',611),('BSA3409',984),('BSA9866',870),('BSA1792',672)]
estoque_fim_mar = [('BSA2199',772),('PPF5239',394),('BSA1212',409),('PPF2154',473),('BEB3410',831),('PPF8999',764),('EMB9591',942),('BSA2006',482),('EMB3604',745),('EMB2070',451),('PPF9018',608),('PPF1468',675),('BSA5819',431),('PPF8666',795),('BEB2983',439),('BEB5877',588),('PPF5008',442),('PPF3877',950),('PPF7321',606),('BSA8833',464),('PPF4980',819),('PPF3063',687),('BSA2089',253),('BSA8398',437),('EMB4622',769),('EMB9814',178),('PPF3784',996),('PPF2398',588),('BEB3211',247),('PPF8655',309),('PPF1874',305),('PPF8789',878),('PPF6324',826),('EMB6618',534),('BSA3409',705),('BSA9895',618),('BSA4319',690)]
estoque_fim_abr = [('BSA2199',647),('PPF5239',292),('BSA1212',551),('PPF2154',802),('BEB3410',712),('PPF8999',603),('EMB9591',963),('BSA2006',481),('EMB3604',199),('EMB2070',635),('PPF9018',956),('PPF1468',161),('BSA5819',787),('PPF8666',771),('BEB2983',867),('BEB5877',539),('PPF5008',614),('PPF3877',715),('PPF7321',336),('BSA8833',961),('PPF4980',116),('PPF3063',876),('BSA2089',579),('BSA8398',814),('EMB4622',434),('EMB9814',981),('PPF3784',498),('PPF2398',498),('BEB3211',606),('PPF8655',168),('PPF1874',518),('PPF8789',157),('PPF6324',501),('EMB6618',932),('BSA3409',247),('BSA9895',287),('BSA4319',477)]

# *listas para dar mais versatilidade, cas outros produtos sejam adicionados em outros meses também
def listar_produtos(*listas):
    # Lista auxiliar
    lista_produtos = []
    # Tivemos que fazer 2 for, pois temos que analisar cada lista e cada produto e estoque dessas listas
    for lista in listas:
        for produto, estoque in lista:
            lista_produtos.append(produto)
        # Botar fora do segundo for, pois ele serve somente para adicionar os produtos na 'lista_produtos'
        # Transformar a lista em set, para removermos os itens repetidos
        lista_produtos = set(lista_produtos)
        # E transformar o set novamente em lista
        lista_produtos = list(lista_produtos)
        return lista_produtos


print(listar_produtos(estoque_fim_jan, estoque_fim_fev, estoque_fim_mar, estoque_fim_abr))