from time import sleep

def tabuada():
    
    multiplicador = int(input("Digite o multiplicador: "))

    multiplicando = 1

    while multiplicando <= 10:
        sleep(1)
        print(multiplicador * multiplicando)
        
        multiplicando += 1

tabuada()