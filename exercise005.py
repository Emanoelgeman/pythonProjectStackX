#Exercise 005: Empresa com 10 funcionários (While)
#Dev: Emanoel G Malheiros
#Data inicio: 09/02/2023.

# código, númeroDeHorasTrabalhadasMês, turnoDeTrabalho (M – matutino; V – vespertino; N – noturno),
# categoria (O – operário; ou G – gerente), valorHoraTrabalhada..

salariominimo = 450
contagemfuncionario = 0
while contagemfuncionario < 10: #loop de funcionarios
    try:
        codigoFuncionario = str(input("Digite o seu Código: "))
        while True:
            try:
                horasTrabalhadas = float(input("Digite o número de horas trabalhas no mês: "))
                break
            except ValueError:
                print("Entrada de dados inválida. Digite um número válido")

        while True:

            turnoDeTrabalho = str(input("Digite o seu turno de trabalho, M, V ou N:"))
            if len(turnoDeTrabalho) == 1 and turnoDeTrabalho == "M" or turnoDeTrabalho == "V" or turnoDeTrabalho == "N":
                break
            print("Turno inválido. Digite M, V ou N.")

        while True:

            categoria = str(input("Digite a categoria que você trabalha, O(operário) ou G(gerente):"))
            if len(categoria) == 1 and categoria == "O" or categoria == "G":
                break
            print("Categoria inválida. Digite O ou V.")

        if categoria == "G" and turnoDeTrabalho == "N":
            valorHoraTrabalhada = salariominimo * 0.18
        elif categoria == "G" and turnoDeTrabalho == "M" or turnoDeTrabalho == "V":
            valorHoraTrabalhada = salariominimo * 0.15
        elif categoria == "O" and turnoDeTrabalho == "N":
            valorHoraTrabalhada = salariominimo * 0.13
        else:
            categoria == "O" and turnoDeTrabalho == "V" or turnoDeTrabalho == "M" # O e V não está indo a hora trabalhada correta.
            valorHoraTrabalhada = salariominimo * 0.10

        salarioinicial = valorHoraTrabalhada * horasTrabalhadas

        if salarioinicial < 300:
            auxilioalimentacao = salarioinicial * 0.20
        elif salarioinicial >= 300 and salarioinicial <= 600:
            auxilioalimentacao = salarioinicial * 0.15
        else:
            salarioinicial > 600
            auxilioalimentacao = salarioinicial * 0.05

        salariofinal = salarioinicial + auxilioalimentacao

        print(codigoFuncionario,"você trabalhou:",int(horasTrabalhadas),"horas,","cada hora sendo: R$",valorHoraTrabalhada)
        print("com um salário inicial de: R$",salarioinicial,"mais um auxilio de: R$",auxilioalimentacao)
        print("totalizando: R$",salariofinal)






    finally: contagemfuncionario +=1


