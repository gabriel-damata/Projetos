# Funções lambda(anônimas)
#Sintaxe:
#lambda argumentos: expressão

# quadrado = lambda x: x ** 2

# for i in range(1, 10):
#     print(quadrado(i))

# par = lambda x: x % 2 == 0

# f_c = lambda f: (f-32) * 5/9

# print(f_c(32))

# Função map()
#Sintaxe:
# map(função, iterável)

# num = [1, 2, 3, 4, 5, 6, 7, 8]
# dobro = list(map(lambda x: x * 2, num))
# print(dobro)

# Função filter()
#Sintaxe:
# filter(função, iterável)

# def numeros_pares(n):
#     return n % 2 == 0

# num = [1, 2, 3, 4, 5, 6, 7, 8]
# pares = list(filter(numeros_pares, num))
# print(pares)

#função reduce()
#Sintaxe:
# reduce(função, sequência)
from functools import reduce

# def mult(x, y):
#     return x * y

# num = [1, 2, 3, 4, 5, 6]
# mult = reduce(mult, num)
# print(mult)