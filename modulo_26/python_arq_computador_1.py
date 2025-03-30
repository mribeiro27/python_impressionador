from pathlib import Path

# Para descobrir o caminho do arquivo que estamos usando: print(Path.cwd())
'''print(Path.cwd())'''

# Ao indicar o Path, trocar as contra barras para barras normais. Quando printarmos a var "caminho", ele rpinta com contra barra
caminho = Path('C:/Users/322070/OneDrive - OPEN LABS S.A/Área de Trabalho/python_impressionador/modulo_26/Arquivos_Lojas')

# Para listarmos os arquivos de uma pasta, usar: Path.iterdir(). Se tentarmos printar, não vai dar certo, pois é um objeto. Para que todos os arquivos sejam listados no terminal, usar o for
arquivos_listados = caminho.iterdir()
# print(arquivos_listados)

'''for arquivo in arquivos_listados:
    print(arquivo) # Não está printando'''

# Verificar se o arquivo existe na pasta

'''if Path('C:/Users/322070/OneDrive - OPEN LABS S.A/Área de Trabalho/python_impressionador/modulo_26/Arquivos_Lojas/201801_Bourbon_SP.csv').exists:
# Como já temos a variável "caminho" com todo o path, iremos botar só o que resta da seguinte maneira:

if (caminho / Path('201801_Bourbon_SP.csv')).exists:
    print("Existe")'''

# Criando uma nova pasta
# Path("Pasta Auxiliar/Pasta Auxiliar 2").mkdir()

# Copiar um arquivo de uma pasta para outra: método shutil
import shutil

arquivo_copiado = (caminho / Path('Arquivos_Lojas/201801_Amazonas Shopping_AM.csv'))
# pasta_destino = Path('Pasta Auxiliar/201801_Amazonas Shopping_AM_versao.csv')
# shutil.copy2(arquivo_copiado, pasta_destino)'''

# Mover um arquivo de um lugar para o outro:
    # shutil.move(arquivo_para_mover, arquivo_onde_colar)

pasta_destino = Path('Pasta Auxiliar/201801_Amazonas Shopping_AM_versao_movido.csv')
shutil.move(arquivo_copiado, pasta_destino)
