# and, or e not

10 is 11

lista_teste = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lista_teste:
    if i == lista_teste[i] + 1:
        lista_teste.pop(i)

print(lista_teste)