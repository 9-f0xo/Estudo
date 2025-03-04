numExtensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    try: 
        num = int(input('Insira um valor de 0 a 20 inteiro: '))

    except ValueError:
        print('Tente novamente, o número precisa ser um valor inteiro.')
        continue

    if num not in range(21):
        print('Tente novamente, precisa ser um valor de 0 a 20.')

    else:
        break

print(f'{num} por extenso é "{numExtensos[num]}". ')