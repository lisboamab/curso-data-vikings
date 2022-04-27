from datetime import date, datetime

hoje = date.today()

ano = int(input("Qual é o ano, no formado 0000, que você está hoje? "))

mes = int(input("Qual é o mês do seu aniversario? (no formato 00) "))

dia = int(input("Qual é o dia do seu aniversario? "))


aniversario = date(ano, mes, dia)

print(f"Faltam {hoje - aniversario} dias para seu aniversario!")