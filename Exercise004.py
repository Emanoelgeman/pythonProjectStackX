#Exercise 004: Salário bruto (IF)
#Dev: Emanoel G Malheiros
#Data inicio: 08/02/2023

while True:
    try:
        salariobruto = float(input("Digite o seu Salário Bruto: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
imposto = float(0.93)

if salariobruto <= 350:
    salariototal= salariobruto * imposto + 100
    print("O seu salário total é de:",salariototal)

elif salariobruto >=351 and salariobruto <=600:
    salariototal= salariobruto * imposto + 75
    print("O seu salário total é de:",salariototal)

elif salariobruto >=601 and salariobruto <=900:
    salariototal= salariobruto * imposto + 50
    print("O seu salário total é de:",salariototal)

else:
    salariototal= salariobruto * imposto + 35
    print("O seu salário total é de:",salariototal)




