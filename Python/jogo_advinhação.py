import random
import os

novo_jogo = 's'


while novo_jogo == 's':
    #Apresentação
    print('Bem-vindo ao jogo de adivinhação! \n')
    print('Tente adivinhar o número que estou pensando entre 1 e 15. \n')
    #Gerar o número aleatório
    valor = random.randint(1, 15)

    #começando o jogo
    input('Pressione Enter para começar...')
    numero = int(input('Digite um número entre 1 e 15: '))

    tentativas = 0

    #Loop para verificar se o número digitado é igual ao valor gerado aleatoriamente
    while numero != valor and tentativas < 3:

        tentativas += 1
        if numero == valor:
            print(f'Parabéns! Vocé acertou o número em {tentativas} tentativas.')
        elif tentativas < 3:
            if numero < valor:
                print('O número que digitou é maior. Tente novamente.')
            elif numero > valor:
                print('O número que estou pensando é menor. Tente novamente.')
            numero = int(input('Digite um número entre 1 e 15: '))
        else:
            print('Você atingiu o número máximo de tentativas. O número correto era:', valor)

    print(f'Parabéns! Você acertou o número em {tentativas} tentativas.')

    #Loop para perguntar se o jogador deseja jogar novamente
    novo_jogo = input('Deseja jogar novamente? (s/n) ')

    #Limpar a tela
    os.system('cls')