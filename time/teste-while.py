from time import sleep

inicio = (int(input("De qual número você quer partir? ")))

fim = (int(input("Digite até onde você quer contar ")))

intervalo = (int(input("Qual é o intervalo que você quer entre os números contados? ")))

if inicio <= fim:
    while inicio <= fim:
        print(inicio)
        sleep(1)
        inicio += intervalo
    print("FIM!")
elif inicio >= fim:
    while inicio >= fim:
        print(inicio)
        sleep(1)
        inicio -= intervalo
    print("FIM!")