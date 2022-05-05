nome = str(input('Digite um nome completo: ')).strip()


print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Se primeiro nome tem {} letras'.format(nome.find(' ')))
separaNomes = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separaNomes[0], len(separaNomes[0])))