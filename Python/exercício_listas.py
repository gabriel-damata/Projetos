# Crie um script que peça para o usuário ddigitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista. Na sequência exiba na tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repatição for.

bebidas = []

for i in range(5):
    bebida = input('Digite uma bebida: ')
    bebidas.append(bebida)

bebidas.sort()

print('\nBebidas favoritas em ordem alfabética: ')
for bebida in bebidas:
    print(bebida)