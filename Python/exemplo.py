import os

#informando o caminho do diretório
diretorio = r'C:\Users\Gabriel\Desktop\python'

if os.path.exists(diretorio):
    arquivos = os.listdir(diretorio)
    print(f'Arquivos no diretório: {arquivos}')

    arquivo_especifico = "meu_arquivo.txt"

    if os.path.exists(os.path.join(diretorio, arquivo_especifico)):
        print(f'O arquivo "{arquivo_especifico}" existe no diretório.')
    else:
        print(f'O arquivo "{arquivo_especifico}" não existe no diretório.')
else:
    print(f'O diretório "{diretorio}" não existe.')