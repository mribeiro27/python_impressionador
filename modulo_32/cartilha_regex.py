'''
### Operadores

    [] – conjunto de  caracteres;
    \ – sequência especial de caracteres;
    ^ – buscar elementos no início da string;
    $ – buscar elementos no final da string;
    * – buscar zero ou mais repetições de uma substring;
    + – uma ou mais aparições de uma substring;
    ? – zero ou uma aparição;
    | – busca um caractere ou outro.
    {} - quantidade específica de caracteres
    [^] - diferente de um caractere especificado logo após o ^
    () - apenas para agrupar regras e definir ordem de aplicação (igual matemática)

### Especificando caracteres:
    . - qualquer caractere
    \d - qualquer dígito
    \D - não é dígito
    \w - qualquer alfanumérico
    \W - não é alfanumérico
    \s - espaço em branco
    \S - não é espaço em branco

#### obs: lembre de usar a string como raw string

### Funções
#### Lembre sempre de importar a biblioteca re

- re.compile('padrao_regex') -> compilar um padrão regex
- re.search(padrao_compilado, texto) -> procura uma ocorrência do padrão no texto (re.match só procura na 1ª linha do texto)
- re.findall(padrao_compilado, texto) -> encontra todas as ocorrencias do padrão em um texto - armazena em uma lista
- re.finditer(padrao_compilado, texto) -> encontra todas as ocorrencias e armazena em um iterador
'''

import re

texto = """
Bom dia,

Seguem os orçamentos solicitados:

Cerveja importada (330 ml) - R$12,30598615178 - bebida
Cerveja nacional (0,5 litros) - R$6,10 - bebida
Garrafa de vinho (750ml) - R$39,90 - bebida
Água (garrafa de 1,5 litros) - R$3,30 - bebida
Alface (1 unidade) - R$3,50 - comida
Cebolas (1kg) - R$5,10 - comida
Batatas (1 kg) - R$5,20 - comida
Tomates (1 kg) - R$7,90 - comida
Laranjas (1 kg) - R$4,70 - comida
Bananas (1kg) - R$5,50 - comida
Maçãs (1 kg) - R$8,30 - comida
Queijo fresco (1 kg) - R$42,90 - comida
Uma dúzia de ovos(12) - R$9,80 - comida
Arroz (1 kg) - R$5,70 - comida
Um quilo de pão (1 kg) - R$7,20 - comida
Leite (1 litro) - R$5,20 - bebida
Azeite (1 unidade) - R$20 - tempero
Pimenta Reino (20g) - R$5 - tempero

Favor informar as quantidades desejadas 
para emissão da Nota Fiscal.

Att.,"""

## Com o Regex, somos capaz de extrair, do texto abaixo, a quantidade de itens de comida e bebidas

# Compilando um padrão. No findall(), devemos passar o padrão e depois onde usar esse padrão
'''padrao = re.compile("comida")
resultado = re.findall(padrao, texto)
print(len(resultado))

padrao = re.compile("bebida")
resultado = re.findall(padrao, texto)
print(len(resultado))'''

# Usando search(): ele dá mais informações quando impresso. Ele mostra apenas a primeira ococrrência, mostra, respectivamente: span (ou seja, o número do carater da primeira e da última letra da palavra) e o match (palavra que foi buscada)
'''padrao = re.compile("comida")
resultado = re.search(padrao, texto)
print(resultado)

padrao = re.compile("bebida")
resultado = re.search(padrao, texto)
print(resultado)'''

# Usando finditer(): encontrará a palavra e criará um iterador (um objeto que conseguimos iterar - usar o "for"). Aqui aparecem as mesmas infos do "search()", mas com as informações de todas as ocorrências das palavras
'''padrao = re.compile("comida")
resultado = re.finditer(padrao, texto)
# print(resultado)

for item in resultado:
    print(item)

padrao = re.compile("bebida")
resultado = re.finditer(padrao, texto)
# print(resultado)

for item in resultado:
    print(item)'''

## Descobrindo quantos produtos há na lista através do "$"

# Para pegar o caracter "$", sem ser o valor especial dele, devemos usar uma contrabarra
'''padrao = re.compile("\$")
resultado = re.findall(padrao, texto)
print(len(resultado))'''

## Extrair números que estão no texto (litros, pesos e preços)

# Nesse caso, devemos especificar carateres e também o "r" (raw string), pois é uma boa prática para caracteres específicos.
# O primeiro número do exemplo é 330. Se botássemos "\d\d" no padrão, uma lista com [33, 12...] seria impressa, pois o padrão agora virou qualquer dígito que seja acompanhado por outro dígito 
# Com o "+" depois do "\d", ele pegará todos os números, independente do número de dígitos. Como os números têm vírgula, iremos fazer da seguinte forma: (r"\d+, \d+"). Entretanto, fazendo isso, apenas os números com vírgula estão sendo impressos
# Só que, com o "+" no segundo, ele impede que números com apenas 1 dígito sejam impressos, pois assim ele indica que apenas números com vírgula sejam impressos
# Para que todos os números, de todos os tipos, sejam impressos, bota-se um "?" antes da vírgula, pois isso indica que haverá 0 ou uma aparição depois da vírgula
padrao = re.compile(r"\d+,?\d*")
resultado = re.findall(padrao, texto)
print(resultado)

novo_texto = "Nome: Jane Doe Idade: 42 Salario: 10000"
# Para conseguir pegar qualquer sequência de caracteres, incluindo o ":" e os espaços, imprimindo exatamente a string inteira
'''padrao = re.compile(r".+")
resultado = re.findall(padrao, novo_texto)
print(resultado)'''

# Pegando só os rótulos (Nome, Idade, Salario)
'''padrao = re.compile(r"\w+:")
resultado = re.findall(padrao, novo_texto)
print(resultado)'''

# Pegando os rótulos sem ":", agrupando uma regra
'''padrao = re.compile(r"(\w+):")
resultado = re.findall(padrao, novo_texto)
print(resultado)'''

## Pegar quantas ml há no primeiro item
# Procurando os caracteres de parêntesis
padrao = re.compile(r"(\(.+\))")
resultado = re.search(padrao, texto)
print(resultado)