# Calculadora em Python


while True:

    print("Bem vindo a Calculadora em Python")
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))

    print("Selecione a operação que voce deseja fazer")
    print("0 = Cancelar")
    print("1 = Soma")
    print("2 = Subtração")
    print("3 = Multiplicação")
    print("4 = Divisão")
    print("5 = Contador de 0 a 100")

    operacao = int(input("Seleção de operação: "))

    match operacao:
        case 0: 
            print("Programa encerrado")
            break
        
        case 1: 
            soma = numero1 + numero2
            print("O resultado da sua Soma é:", soma)

        case 2: 
            subtracao = numero1 - numero2
            print("O resultado da sua subtração:", subtracao)

        case 3:
            multiplicacao = numero1 * numero2
            print("O resultado da sua multiplicação é:", multiplicacao)

        case 4:
            divisao = numero1 / numero2
            print("O resultado da sua divisão é:", divisao)

        case 5: 
            for i in range(0, 101):
                print(i)

        case _: 
            print("Erro opção invalidade, tente denovo.")
            continue