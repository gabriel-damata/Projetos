import random

# valor = random.randint(1,20)
# print(valor)

# print ('Gerar cinco números aleatórios entre 1 e 50: \n')

# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado: {n}')

l = [2, 4,6,9,10,13,14,16,18,20,21,27,33]
n = random.choice(l)
print(f'Número escolhido: {n}')

m = random.sample(l, 3)
print(f'Lista de números escolhidos: {m}')

#embaralhar uma lista
print(f'Exibir a lista original: {l}')
print(f'Embaralhar a lista e exibi-la:')
o = random.shuffle(l)
print(l)