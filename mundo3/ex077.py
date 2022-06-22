palavras = ('aprender', 'programa', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\n Na palavra {palavra} temos a seguintes vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
