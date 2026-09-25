from modules.lagrange import tabelaDePontos, interpolar_todas_combinacoes, desvio_relativo_percentual, erro_trucamento

if __name__ == '__main__':

    X,Y = tabelaDePontos()
    x_alvo = input("digite o valor do ponto que quer interpolar\n ")
    resultado = interpolar_todas_combinacoes(X, Y, x_alvo)
    funcao = input("digite a funcao se quiser o erro de trucamneto, se nao, digite -1\n")
    if funcao != -1:
        print(f'Os resultados foram {resultado}\nO DRP é {desvio_relativo_percentual(resultado, x_alvo)}\nO erro de trucamento é {erro_trucamento(funcao, x_alvo, X)}')
    print(f'Os resultados foram {resultado}\nO DRP é {desvio_relativo_percentual(resultado, x_alvo)}\n')