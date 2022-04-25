
respostas = []

respostas.append(input(f"\nDigite seu nome:"))

respostas.append(int(input(f"\nDigite sua idade")))

respostas.append(input(f"\nDigite seu e-mail"))


nome, idade, email = respostas

print(f"\n Olá {nome} que legal, você tem {idade} anos! Posso confirmar o e-mail {email}?")