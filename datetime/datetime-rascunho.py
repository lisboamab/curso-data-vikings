from datetime import *

diadePagamento = datetime(2022, 4, 27)
print(type(diadePagamento))

diadePagamentoBR = diadePagamento.strftime('%d/%m/%y')

proximoPagamento = diadePagamento + timedelta(days=30)
proximoPagamentoBR = proximoPagamento.strftime('%d/%m/%y')

print(f" O dia do pagamento foi {diadePagamentoBR} o proximo pagamento será {proximoPagamentoBR}")




