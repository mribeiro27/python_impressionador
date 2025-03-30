print("O que fica dentro dos parêntesis é um argumento/parêmetro!")

# Vamos supor que esteja analisando uma lista de produtos, dezenas delas. Se quisermos criar uma function pra analisar desta lista, é interessante que a function receba a lista como argumento para realizar a análise: versátil, pois dá pra fazer várias vezes

# O print mesmo pode receber vários parâmetros:
vendas = 50
print(f"Produto", "iPhone", "Vendas", vendas)

# Os parâmetros devem ser como variáveis: nessa, a function recebe 3 números e retorna a soma destes

def minha_soma(num1, num2, num3):
    return num1 + num2 + num3

# É melhor atribuir a chamada da função à uma variável
# Os valores, em ordem, se tornam as vars de num. Se passássemos só 2 parâmetros, iria dar erro, pois deve seguir o número de variáveis
soma = minha_soma(50, 20, 30)
print(soma)

