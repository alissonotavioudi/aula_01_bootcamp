#Questão: Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

CONSTANTE_BONUS = 1000

# 1 - O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Digite seu nome: ")

# 2- Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input("Digite seu salario: "))

# 3 - Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_salario = float(input("Digite seu bonus: "))

# 4 - O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
valor_bonus = CONSTANTE_BONUS + salario * bonus_salario
# 5 - Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 7000".
print(f"O usuário {nome} possui o bonus de {valor_bonus}. ")