#Funções
# Modularizaçã, reúso de código, legibilidade

# def <nome_da_funcao>([argumentos]):
#     <intruções> 

# def mensagem():
#     print('Bóson Treinamentos em Tecnologia!\n')
#     print('Bem vindo ao curso de Python!')


# mensagem()

# def soma(a, b):
#     print(a + b)

# soma(12, 7)

# def mult(x, y):
#     return x * y

# a = 5
# b = 8
# c = mult(a, b)
# print(f'O produto de {a} e {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossível dividir por zero!'

# def contar(num = 11, caractere = '+'):
#     for i in range(1, num):
#         print(caractere)

x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
   if c == 0:
      return a * b
   else:
      return a + b + c

if __name__ == '__main__':
   res = soma_mult(x, y, z)
   print(res)
  