from random import *
from string import *

caracteres = digits + ascii_letters + punctuation

senha = "".join(choice(caracteres) for _ in range(20))

print(senha)
