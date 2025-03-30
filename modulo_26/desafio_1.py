from pathlib import Path
import shutil

# Criando pastas com for
'''estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
for estado in estados:
    Path("Arquivos_Lojas/{}".format(estado)).mkdir()'''

# Criando as pastas de acordo com o estado 
'''Path("Arquivos_Lojas/RJ").mkdir()
Path("Arquivos_Lojas/SP").mkdir()
Path("Arquivos_Lojas/MG").mkdir()
Path("Arquivos_Lojas/GO").mkdir()
Path("Arquivos_Lojas/AM").mkdir()'''

# Path da pasta com as planilhas das lojas necessárias
caminho = Path('Arquivos_Lojas/')
# Movendo as planilhas das lojas
arquivos = caminho.iterdir()

for arquivo in arquivos:
    nome_arquivo = arquivo.name
    # Verificar se o arquivo termina com .csv
    if nome_arquivo[-3:] == 'csv':
        # Através da sigla do estado, pegar os arquivos para botar nas pastas destino
        estado = nome_arquivo[-6:-4]
        # Como o nome do arquivo varia de acordo com o estado, e há pastas diferentes, iremos usar chaves para representar a pasta (estado) e os arquivos (nome_arquivo)
        local_final = caminho / Path("{}/{}".format(estado, nome_arquivo))
        shutil.move(arquivo, local_final)