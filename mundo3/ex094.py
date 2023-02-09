pessoas_lista = []
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: '))

    while True:
        pessoa['sexo'] = str(input('Digite seu sexo (M/F): ').upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('"ERRO" - por favor digite apenas M ou F' )

    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']

    while True:
        resposta = str(input('Quer continuar S/N?').upper()[0])
        if resposta in 'SN':
            break
        print('"ERRO" - por favor digite apenas S ou N' )

    pessoas_lista.append(pessoa.copy())

    if resposta == 'N':
        break
quant_pessoas = len(pessoas_lista)
print(f'A) Ao todo temos {quant_pessoas} pessoa(s) cadastrada(s)')
media = soma / quant_pessoas
print(f'B) A média das idades cadastradas é {media:5.2f}')
print(f'C) As mulheres cadastradas foram:')
for p in pessoas_lista:
    if p['sexo'] == 'F':
        print(p['nome'])
print(f'D) A lista de pessoas que estão acima da média: ')
for p in pessoas_lista:
    if p['idade'] > media:
        print(p['nome'])

