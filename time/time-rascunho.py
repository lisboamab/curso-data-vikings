from time import *

agora = localtime()

print(strftime('%d/%m/%y %H:%M', agora))
"""
print("Agora vou contar até 10!")
sleep(1)
print("1")
sleep(1)
print("2")
sleep(1)
print("3")
sleep(1)
print("4")
sleep(1)
print("5")
sleep(1)
print("6")
sleep(1)
print("7")
sleep(1)
print("8")
sleep(1)
print("9")
sleep(1)
print("10")

"""

for i in range(1, 11):
    if i == 1:
        print("Agora vou contar até 10!")
    print(i)
    sleep(1)