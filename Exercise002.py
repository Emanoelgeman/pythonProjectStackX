# Exercise 002: Idade e Peso (IF)
# Dev: Emanoel G Malheiros
# Data inicio: 03/02/2023

while True:

    nome = str(input("Digite o seu primerio nome: "))  # ver como fazer para para poder usar o espaço
    if len(nome) > 1 and nome.isalpha():
        break
    print("Entrada inválida. Digite um nome válido.")

while True:
    try:
        idade = int(input("Digite a sua idade: "))  # ver como limitar idade de 0 anos a 100 anos para funcionar
        break
    except ValueError:
        print("Digite uma idade válida.")

while True:
    try:
        peso = float(input("Digite o seu peso em KG: "))  # ver como limitar peso de 0 a 200
        break
    except ValueError:
        print("Digite um peso valido ")

# menores de 20 anos
if idade < 20 and peso <= 60:
    print(nome, ", você se encontra no grupo de risco: 9")
if idade < 20 and peso > 60 and peso <= 90:
    print(nome, ", você se encontra no grupo de risco: 8")
if idade < 20 and peso > 90:
    print(nome, ", você se encontra no grupo de risco: 7")

# de 20 a 50 anos
if idade >= 20 and idade <= 50 and peso <= 60:
    print(nome, ", você se encontra no grupo de risco: 6")
if idade >= 20 and idade <= 50 and peso > 60 and peso <= 90:
    print(nome, ", você se encontra no grupo de risco: 5")
if idade >= 20 and idade <= 50 and peso > 90:
    print(nome, ", você se encontra no grupo de risco: 4")

# maiores que 50 anos
if idade > 50 and peso <= 60:
    print(nome, ", você se encontra no grupo de risco: 3")
if idade > 50 and peso > 60 and peso <= 90:
    print(nome, ", você se encontra no grupo de risco: 2")
if idade > 50 and peso > 90:
    print(nome, ", você se encontra no grupo de risco: 1")
