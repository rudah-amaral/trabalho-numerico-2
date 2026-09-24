def ler_float(mensagem):
    return float(input(mensagem).replace(",", "."))

def metodoLagrange():
    x_alvo = ler_float("Digite o ponto que você deseja interpolar: ")
    pontos = int(input("Quantos pontos: "))
    X, Y = [], []

    for i in range(pontos):
        X.append(ler_float(f"x{i} = "))
        Y.append(ler_float(f"y{i} = "))

    coeficientes = []
    for indice in range(pontos):
        L = 1
        for j in range(len(X)):
            if indice != j:
                L *= (x_alvo - X[j])/(X[indice] - X[j])
        coeficientes.append(L)

    pn = 0
    for i in range(len(Y)):
        pn += coeficientes[i]*Y[i]

    print(f"p({x_alvo}) = {pn}")

metodoLagrange()