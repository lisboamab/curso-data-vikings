
respostas = []

respostas.append(input(f"\nDigite seu nome:"))

respostas.append(int(input(f"\nDigite sua idade")))

respostas.append(input(f"\nDigite seu e-mail"))


nome, idade, email = respostas

#o 'f' antes das aspas faz a função do antigo .format do python, possibilita fazer operações e colocar váriaveis dentro de strings.
print(f"\n Olá {nome} que legal, você tem {idade} anos! Posso confirmar o e-mail {email}?")