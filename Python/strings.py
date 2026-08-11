# nome = 'Curso de Python'
# instrutor = 'Gabriel'
# print(nome + ' com ' + instrutor) #Concatenação de strings

#frase = 'Vamos aprender Python hoje.'
# palavras = frase.split() #Divide a frase em palavras
# print(palavras) #Exibe a lista de palavras
#print(frase[6:15])

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)#Verifica se a palavra existe na frase
# print('magnésio' in produtos)#Verifica se a palavra existe na frase

fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20)) #Alinha a string à direita
print(fruta.center(20)) #Alinha a string no centro
print(fruta.ljust(20, "-")) #Alinha a string à esquerda
print(fruta.center(20, "-")) #Alinha a string no centro

# Docstrings: são strings que servem para documentar funções, classes e métodos. Elas são definidas entre três aspas simples ou duplas e podem se estender por várias linhas. O Python utiliza docstrings para gerar documentação automática do código.
texto ="""
Docstring é uma espécie de documantação
que podemos inserir dentro de um módulo, função
ou classe no Python, entre outros locais.
    Respeita o deslocamento de texto e é    multilinhas
"""
print(texto)
