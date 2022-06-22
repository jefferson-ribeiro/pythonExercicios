"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

times = ('Palmeiras', 'Corinthians', 'Internacional', 'Athlético-PR', 'São Paulo', 'Atlético-MG', 'Avaí', 'Santos',
         'Red Bull Bragantino', 'Flamengo', 'Fluminense', 'Curitiba', 'América-MG', 'Botafogo', 'Ceará', 'Goiás',
         'Atlético-GO', 'Cuiabá', 'Juventude', 'Fortaleza')

print('Segue os 5 primeiros colocados: ')
print(times[0:5])
for i in range(0, 5):
    print(f'Este é o {i+1}º colocado: - {times[i]}')

print('='*20)
print('Segue os 4 últimos colocados: ')
print(times[-4:])
for i in range(19, 15, -1):
    print(f'Este é o {i+1}º colocado: - {times[i]}')

print('='*20)
print('Segue times em ordem alfabética')
print(sorted(times))

print('='*20)
print(f'O Red Bull Bragantino está na posição: {times.index("Red Bull Bragantino")+1}')
print()

