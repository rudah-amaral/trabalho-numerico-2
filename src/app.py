from modules.lagrange import tabelaDePontos, interpolar_todas_combinacoes, desvio_relativo_percentual, ler_float, erro_truncamento
from modules.expressoes import criar_funcao

def main():

    X,Y = tabelaDePontos()
    x_alvo = ler_float("digite o valor do ponto que quer interpolar\n ")

    resultado = interpolar_todas_combinacoes(X, Y, x_alvo)
    funcao = input("digite a funcao se quiser o erro de trucamneto, se nao, digite -1\n")

    if funcao != "-1":
        funcao_python = criar_funcao(funcao)
        referenciaPython = funcao_python(x_alvo)
        print(f'Os resultados foram {resultado}\nO DRP é {desvio_relativo_percentual(resultado, x_alvo)}\nO erro de trucamento é {erro_truncamento(funcao, x_alvo, X)}')
        print(f'Os resultados foram {resultado}\nO DRP é {desvio_relativo_percentual(resultado, referenciaPython)}\n')
    else:
        referencia = ler_float("digite o valor de referencia\n")
        print(f'Os resultados foram {resultado}\nO DRP é {desvio_relativo_percentual(resultado, referencia)}\n')

if __name__ == '__main__':
    main()