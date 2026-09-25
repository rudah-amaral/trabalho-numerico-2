from itertools import combinations
from modules.expressoes import ExpressaoInvalidaError, criar_derivada, criar_funcao

#Vamos ter que criar um função para interpretar funções (já temos isso pronto)
#para ficar mais dinamico, só do hermes colocar o x_alvo e a função o nosso programa vai saber a imagem desejada
#lagrange funciona assim??? (não lembro direito)
#para não correr nenhum risco de perder valores importantes, a gnt vai precisar ser bem redundante
#amanhã eu vou fazer o neville

def ler_float(mensagem):
    return float(input(mensagem).replace(",", "."))

def tabelaDePontos():
    n = int(input("quantos pontos terá sua tabela"))
    X,Y = [], []
    print ('digite os valores de x, depois aperte enter para digitar os valores de y\n')
    for i in range(n):
        X.append(ler_float(f"x{i} = "))
        Y.append(ler_float(f"y{i} = "))
        if len(set(X)) != len(X):
            raise ValueError ("os valores de x devem ser diferentes")
        if len(Y) != len(X):
            raise ValueError ("a quantidade de valores de y devem ser da mesma quantidade de valores de x")

    return X,Y



def neville(X, Y, x_alvo):
    n = len(X)
    q = [[0.0] * n for _ in range(n)]
    for i in range(n):
        q[i][0] = Y[i]


    for i in range(1, n):
        for j in range(i, n):
           # q[i][j] = ((x_alvo - X[j - i]*q[j][i-1]) - (x_alvo - X[j]*q[j-1][i-1])/ (X[j]- X[j-i]))
           # Fórmula de Neville corrigida matematicamente e com conversão forçada para float
           q[i][j] = ((float(x_alvo) - float(X[j - i])) * q[j][i - 1] - (float(x_alvo) - float(X[j])) * q[j - 1][i - 1]) / (float(X[j]) - float(X[j - i]))

    return q[n-1][n-1]


def interpolar_todas_combinacoes(X,Y, x_alvo) -> list[float]:
    resultados = []
    n = len(X)

    for tamanho in range(2, n+1):
        for indices in combinations (range(n), tamanho):
            sub_X = [X[i] for i in indices]
            sub_Y = [Y[i] for i in indices]
            resultados.append((indices, neville(sub_X, sub_Y, x_alvo)))

    return resultados

def desvio_relativo_percentual(resultados, referencia) -> list[float]:
    DRP = []
    # res[1] é o valor numérico gerado pelo neville, res[0] são os índices
    for res in resultados:
        valor_calculado = res[1]
        desvio = abs((valor_calculado - referencia) / referencia) * 100
        DRP.append(desvio)
    return DRP

def erro_truncamento(funcao, x_alvo, X):

    funcao_ = criar_funcao(funcao)

    n_pontos = len(X)

    # derivada de ordem n_pontos
    df = funcao_
    for _ in range(n_pontos):
        df = criar_derivada(df)

    produto = 1
    fatorial = 1
    try:
        for i in range(n_pontos):
            produto *= (x_alvo - X[i])
            fatorial *= (i + 1)
    except Exception as e:
        raise ExpressaoInvalidaError(f"Não foi possível calcular o produto para x_alvo={x_alvo}: {e}") from e

    min_ = min(X)
    max_ = max(X)

    try:
        erro = max(abs(produto * df(max_) / fatorial), abs(produto * df(min_) / fatorial))
    except Exception as e:
        raise ExpressaoInvalidaError(f"Não foi possível calcular a derivada de ordem {len(X)} para x_alvo={x_alvo}: {e}") from e

    return erro


