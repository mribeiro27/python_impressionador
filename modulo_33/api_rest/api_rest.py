# Para criarmos uma API, precisamos de um servidor (a API é como se fosse um microsite). Há 2 formas de criar sites em Python: Django e Flask (melhor para criar APIs. É uma ferramenta de microsserviços em Python)

## Iniciando com Flask: criação de API "A Minimal Application"
from flask import Flask
import pandas as pd

tabela = pd.read_excel(r'C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_33\api_rest\Vendas - Dez.xlsx')

# Inicialização da API no Flask (criação site)
app = Flask(__name__)

'''# As funcionalidades da API (site) são ditadas pelo decorator e por uma função
@app.route("/") # isso é um decorator, que diz em qual link a função irá rodar. Nesse caso, como é só a barra, esse é o link padrão do site
def hello_world(): 
    return {"Olá": "mundo"}

@app.route("/maridopythinho") # Para acessar esse link, basta entrar em http://127.0.0.1:5000/maridopythinho. O endpoint é /maridopythinho
def mari(): 
    return {"Mari": "Pytheira"}

@app.route("/rainhadopython") # Para acessar esse link, basta entrar em http://127.0.0.1:5000/maridopythinho. O endpoint é /rainhadopython
def rainha(): 
    return {"Mari arrasa": "no Python"}

# Botando a API (site) no ar, estando disponível apenas na minha máquina. No caso abaixo, estará rodando em http://127.0.0.1:5000. Esse código transforma a máquina em um servidor'''

# Até agora, isso é um site, dado que uma API nos retorna JSON, que é um dicionário python. Logo, iremos editar os retornos das funções para que sejam dicionários

# Transformando em uma API de faturamento

@app.route("/")
def fat():
    # Qualquer operação que fazemos com tabelas, o resultado sairá em formato de tabela. Para isso, devemos tranformar o resultado em número
    faturamento = float(tabela['Valor Final'].sum())
    return {"faturamento": faturamento}

@app.route("/vendas/produtos")
def vendas_produtos():
    # O código abaixo gera uma tabela do faturamento (valor final) de cada um dos produtos. Como são 2 parâmetros, será uma lista dentro de outra lista aqui. Agrupando cada produto, todas as vezes que eles aparecem, o valor final relacionado a este será somado
    tabela_vendas_produtos = tabela[['Produto', 'Valor Final']].groupby('Produto').sum()
    # Essa tabela gerada será transformada em um dicionário
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

# Ao botarmos "produto" entre <>, isso permite que o usuário pesquise o faturamento de apenas um determinado produto desejado, sem ter que procurá-lo naquela lista 
@app.route("/vendas/produtos/<produto>")
def venda_produtos_especificos(produto): 
    tabela_vendas_produtos = tabela[['Produto', 'Valor Final']].groupby('Produto').sum()
    # Se dentro do índice da tabela (que será a coluna de Produtos), existir o produto desejado, logo
    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    else:
        return {produto: "Inexistente"}
    
app.run()