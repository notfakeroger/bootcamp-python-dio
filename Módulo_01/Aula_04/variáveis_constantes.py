# As variáveis são declaradas da mesma forma que a maioria das linguagens (Eu conheço o JavaScript, então estou acostumado com const e let), porém, em Python, podemos declarar as variáveis na mesma linha, separando-as por vírgula. Segue exemplos abaixo:

name, age = 'Gustavo', 21
print(f'Meu nome é {name} e eu tenho {age} anos de idade!') # Obs.: Aquele "f" que foi colocado antes da aspa simples é usada para facilitar o código, evitando a concatenação e deixando o código mais limpo. Isso é chamado de formatted string literal.

# Para mudar o elemento de alguma variável, basta fazer uma nova atribuição a variável.

name, age = 'Guilherme', 18
print(f"Meu nome é {name} e eu tenho {age} anos de idade!")


# Diferente de algumas linguagens, as constantes são declaradas em maiúsculo em Python. Isso é uma convenção usada pelos programadores Python.

DEBUG = True
BRAZILIAN_STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 1026.41

# Boas Práticas: 

# O padrão de nomes deve ser snake case, ou seja, ao invés de espaços em branco que separam os nomes, usamos o underline. Exemplo: snake_case.

# Escolher nomes sugestivos para as variáveis. Exemplo: name, age, etc.

# Nome de constantes todo em maiúsculo. Exemplo: DEBUG = True