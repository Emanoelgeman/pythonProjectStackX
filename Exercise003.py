#Exercise 003: Idade de um nadador (IF)
#Dev: Emanoel G Malheiros
#Data inicio: 04/02/2023


while True:

        nome = str(input("Digite o seu primeiro nome: "))
        if len(nome) >1 and nome.isalpha():
            break
        print("Entrada inválida. Digite um nome válido: ")

while True:
    try:
        idade = int(input("Digite a sua idade: "))
        break
    except ValueError:
        print("Entrada Inválida. Digite uma idade válida.")

if idade <5:
    print(nome,"infelizmente não temos uma categoria para", idade,"anos de idade.")

if idade >=5 and idade<=7:
    print(nome,"com", idade,"anos de idade, sua categoria é: Infantil.")
if idade >=8 and idade<=10:
    print(nome,"com", idade,"anos de idade, sua categoria é: Juvenil.")
if idade >=11 and idade<=15:
    print(nome,"com", idade,"anos de idade, sua categoria é: Adolescente.")
if idade >=16 and idade<=30:
    print(nome,"com", idade,"anos de idade, sua categoria é: Adulto.")
if idade >30:
    print(nome,"com", idade,"anos de idade, sua categoria é: Sênior.")