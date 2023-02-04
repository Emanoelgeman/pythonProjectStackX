#Exercise 001: Gratificação de natal (IF)
#Dev: Emanoel G Malheiros
#Data inicio: 02/02/2023

while True:
    NomeFuncionario = str(input("Qual o seu primeiro nome?")) #como incluir o nome nas horasextras e trabalhas e como habilitar mais de um nome
    if len(NomeFuncionario) >1 and NomeFuncionario.isalpha():
        break
    print("Nome inválido. Digite um nome válido")
while True:
    try:
        HorasExtrasTrabalhadas = float(input("Quantas horas extras você trabalhou: "))
        break
    except ValueError:
        print("Entrada de dados inválida. Digite um número válido.")

while True:
    try:
        HorasFaltasTrabalhadas = float(input("Quantas horas faltas você teve: "))
        break
    except ValueError:
        print("Entrada de dados inválida. Digite um número válido.")

TotalMinutos = (HorasExtrasTrabalhadas - (2/3*HorasFaltasTrabalhadas)) *60

if TotalMinutos >= 2401:  #descobrir como tirar todos esses elif
    print("Você trabalhou", int(TotalMinutos), "minutos, sua gratificação é de: R$ 500,00")
elif TotalMinutos >= 1801 <2401:
    print("Você trabalhou", int(TotalMinutos), "minutos, sua gratificação é de: R$ 400,00")
elif TotalMinutos >= 1201 <1801:
    print("Você trabalhou", int(TotalMinutos), "minutos, sua gratificação é de: R$ 300,00")
elif TotalMinutos >= 600 <1201:
    print("Você trabalhou", int(TotalMinutos), "minutos, sua gratificação é de: R$ 200,00")
elif TotalMinutos >=1 <600:
    print("Você trabalhou", int(TotalMinutos), "minutos, sua gratificação é de: R$ 100,00")
elif TotalMinutos <=0:
    print("Você trabalhou", int(TotalMinutos), "minutos, você não teve gratificação")