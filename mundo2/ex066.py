"""Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre elas (desconsiderando o flag). """
cont = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} números')
print(f'A soma entre os números digitados é {soma}')

# import json
#
# event = {'Type': 'Notification',
#          'Message': '{"Records": [{"s3": {"bucket": {"name": "teste"}, "object": {"key": "arquivo2.jsonl"}}}]}',
#          'Timestamp': '2012-05-02T00:54:06.655Z'}
#
# list_name_files = []
# list_records = []
#
# for linha in json.loads(event["Message"])["Records"]:
#     # print(linha)
#     list_records.append(linha)
# print(list_records)
#
# # file_message = list(json.loads(event["Message"])["Records"])
#
# for i, linha in enumerate(list_records):
#     name_files = next(iter(linha['s3']['object'].values()))
#     # name_file = list(linha[i]["s3"]["object"].values())[i]
#     list_name_files.append(name_files)
# print(list_name_files)
