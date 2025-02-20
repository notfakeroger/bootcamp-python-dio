# Me "desafiei" a fazer um calculador de média aritmética utilizando Python. Apesar de ser simples, pode ser bom para fixar na minha mente.

nome = input("Informe seu nome: ")
sobrenome = input("Agora, informe seu sobrenome: ")
print(f"Bem vindo, {nome} {sobrenome}! Vamos calcular sua média?")

nota_1 = float(input("Qual foi a sua primeira nota?"))
nota_2 = float(input("Agora, por favor, informe o valor da segunda nota."))
media = (nota_1 + nota_2) / 2

print(f"A sua média é {media}")
 
if media >= 6:
    print(f"Parabéns {nome}, você foi aprovado!")
else:
    print(f"Infelizmente, você foi reprovado, {nome}.")


# Ficou bem básico, mas acho que é suficiente para um começo. Já tenho um pouco de conhecimento por conta de javaScript, usando o console.log, porém achei melhor não ter pressa e ir aprendendo e me desenvolvendo devagar.