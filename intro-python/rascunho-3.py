# and, or e not

10 is 11

lista_teste = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lista_teste:
    if i == lista_teste[i] + 1:
        #pop() é um metodo para list que remove um elemento com base no index dele. Lembrando que em python a indexação inicia em 0.
        lista_teste.pop(i)

#sort() é um metodo aplicado ao tipo list que ordena os elementos da lista, passando o parametro 'reverse=True' a ordem é invertida
lista_teste.sort(reverse=True)

print(lista_teste)

