# Escopo Global e Local

var_global = "Curso Completo de Python"

def escreve_texto():
    var_local = "Fabio Reis"
    print(f'VariávelGlobal: {var_global}')
    print(f'Variável Local: {var_local}')


if __name__ == "__main__":
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print ('Tentar acessar as variáveis diretamente')
    print(f'VariávelGlobal: {var_global}')
    