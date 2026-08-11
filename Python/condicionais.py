# simples, composto, encadeado

n1 = n2 = 0.0
media = 0.0
f = 0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
f = int(input('Digite a quantidade de faltas: '))

# Calcular a média
media = (n1 + n2) / 2

# Exibir o resultado
if (f >= 10):
    print('Aluno Reprovado por Faltas!')
elif (media >= 7):
    print('Resultado:Aprovado!')
    print("Parabéns!")
elif (media >= 5):
    print('Você está de recuperação!')
else:
    print('Aluno Reprovado...')

print('Sua média é {}'.format(media))