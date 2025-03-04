palavras = (
    'Amigos', 'Sabedoria', 'Internacional', 'AEAIAO'
)

vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'Na palavra "{palavra}", temos as vogais:', end=' ')
    
    for vogal in vogais:
        qtd = palavra.lower().count(vogal)  # Conta vogais na palavra (ignora maiúsculas)
        if qtd > 0:
            print(f'{vogal} ({qtd}x)', end=' ')
    
    print()
