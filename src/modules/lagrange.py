from itertools import combinations

#Vamos ter que criar um função para interpretar funções (já temos isso pronto)
#para ficar mais dinamico, só do hermes colocar o x_alvo e a função o nosso programa vai saber a imagem desejada
#lagrange funciona assim??? (não lembro direito)
#para não correr nenhum risco de perder valores importantes, a gnt vai precisar ser bem redundante
#amanhã eu vou fazer o neville

def ler_float(mensagem):
    return float(input(mensagem).replace(",", "."))

def tabelaDePontos(x, y):
    X,Y = [], []

    for i in range(len(X)):
        X.append(ler_float(f"x{i} = "))
        Y.append(ler_float(f"y{i} = "))
        if len(set(X)) != len(X):
            raise ValueError ("os valores de x devem ser diferentes")

    return X,Y


def neville(X, Y, x_alvo) -> float:
    n = len(X)
    q = [[0,0] * n for i in range(n)]
    for i in range(n):
        q[i][0] = Y[i]

    for i in range(1, n):
        for j in range(i, n):
            q[i][j] = ((x_alvo - X[j - i]*q[j][i-1]) - (x_alvo - X[j-1]*q[j-1][i-1])/ (X[j]- X[j-i]))



def interpolar_todas_combinacoes(X,Y, x_alvo) -> list[float]:
    resultados = []
    n = len(X)

    for tamanho in range(2, n+1):
        for indices in combinations (range(n), tamanho):
            sub_X = [X[i] for i in indices]
            sub_Y = [Y[i] for i in indices]
            resultados.append((indices, neville(sub_X, sub_Y, x_alvo)))

    return resultados

def desvio_relativo_percentual( resultados, referencia) -> list[float]:
   return [abs((resultados[i] - referencia) / referencia) * 100 for i in range(resultados)]



