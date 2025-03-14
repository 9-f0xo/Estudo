tabela = (
    'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo',
    'Internacional', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Vasco da Gama',
    'Fluminense', 'Criciúma', 'Grêmio', 'Red Bull Bragantino', 'Juventude',
    'Vitória', 'Corinthians', 'Athletico-PR', 'Cuiabá', 'Atlético-GO'
)


print('-'*25,'\n 5 Primeiros Colocados:')

for indice, colocado in enumerate(tabela[:5]):
    print(indice+1,'º:',colocado)

print('-'*25,'\n 4 Últimos Colocados:')

for indice, colocado in enumerate(tabela[-4:], start=len(tabela) - 3):
    print(indice+1,'º:',colocado)

print('-'*25,'\n Tabela Em Ordem Alfabética:')

for colocado in sorted(tabela):
    print(colocado)