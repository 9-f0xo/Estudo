an = 500
a1 = 100
r3 = 3
r7 = 7
r21 = 21  # Múltiplo comum de 3 e 7

def progressao_aritimetica(an, a1, r):
    n = ((an - a1) / r) + 1
    return round(n)  # Arredondamento para baixo garante números inteiros

div3 = progressao_aritimetica(an, a1, r3)
div7 = progressao_aritimetica(an, a1, r7)
div21 = progressao_aritimetica(an, a1, r21)  # Evita contagem dupla

res = div3 + div7 - div21  # Corrige a soma
nao_divisiveis = (an - a1 + 1) - res  # Total de números - divisíveis

print(f'Quantidade de números divisíveis por 3: {div3}')
print(f'Quantidade de números divisíveis por 7: {div7}')
print(f'Quantidade de números divisíveis por 3 e 7 ao mesmo tempo: {div21}')
print(f'Total de números divisíveis por 3 ou 7: {res}')
print(f'Quantidade de números que NÃO são divisíveis por 3 nem por 7: {nao_divisiveis}')
