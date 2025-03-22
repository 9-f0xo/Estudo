contador = 0

def verificar_numero(numero):
    if (numero%3>0) and (numero%7>0):
        return True
    else:
        return False

for numero in range(100,500):
    if verificar_numero(numero):
        print(numero)
        contador +=1

print(contador)
