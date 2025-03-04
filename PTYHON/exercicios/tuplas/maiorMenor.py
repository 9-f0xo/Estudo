import random

tuplaNum = (random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))

print(f' Números gerados: {tuplaNum}')

tuplaNum = sorted(tuplaNum)

print(f'Números ordenados: {tuplaNum}')

print('Menor número: ',min(tuplaNum))
print('Maior número: ',max(tuplaNum))
