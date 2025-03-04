produtos = (
    'Alvejante', 12.99, 'Fezes Frescas', 2.99, 'Chocolate HIPER Hidrogenado', 0.50, 'Banana Prata', 52.90
)

# Cabeçalho formatado
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # Centraliza o título
print('-' * 40)

for i in range(0, len(produtos), 2): # Vai de 2 em 2 para acessar em pares

    nome = produtos[i]
    preco = produtos[i+1]

    print(f'{nome.ljust(30, ".")}R$ {preco:>6.2f}')  # Formatação alinhada

print('-' * 40)