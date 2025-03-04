while True:
    try:
        tupla = tuple(int(input(f'Insira o {i+1}º valor: ')) for i in range(4))
        break

    except ValueError:
        print('Precisa ser um valor inteiro.')

print(f'\nTupla gerada: {tupla}')

print(f'Quantas vezes o número 9 aparece? {tupla.count(9)}')

if 3 in tupla:
    print(f'Qual foi a posição em que o três apareceu pela primeira vez? {tupla.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado.')
    

for valor in tupla:
    if valor %2 == 0:
        print(f'{valor} é um número par.')
    else:
        print(f'{valor} é um número ímpar.')


#Alternativa:

# pares = [num for num in tupla if num % 2 == 0]
# if pares:
#     print(f'Números pares encontrados: {pares}')
# else:
#     print('Nenhum número par foi digitado.')