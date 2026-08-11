import os
import shutil

diretorio_principal ='C:\\Users\\Gabriel\\Desktop\\python' #Substitua pelo caminho do seu diretório
diretorio_destino = {"pdf": "Documentos", "jpg": "Imagens", "txt": "Textos"} 

for filename in os.listdir(diretorio_principal):
    base, ext = os.path.splitext(filename) #Separa nome do arquivo e extensão
    ext = ext.lower() #Converte a extensão para minúscula para comparação
    if ext in diretorio_destino:
        destino = os.path.join(diretorio_principal, diretorio_destino[ext]) #Cria o caminho do diretório de destino
        if not os.path.exists(destino):
            os.makedirs(destino) #Cria o diretório de destino se ele ainda não existir
        #caminho_arquivo = os.path.join(diretorio_principal, filename) #Cria o caminho completo do arquivo
        shutil.move(os.path.join(diretorio_principal, filename), destino) #Move o arquivo para o diretório de destino
        print(f"Arquivo {filename} movido para {destino}")
        