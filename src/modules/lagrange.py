from dataclasses import dataclass

@dataclass
class Ponto:
    x: int # coordenada no eixo x
    y: int # a imagem da função, coordenada no eixo y

def interpolar_dois_pontos(pontos: list[Ponto], x_alvo) -> list[float]:
    valores = []
    n = len(pontos)
    for i in range(n):
        for j in range(n):
            if j != i:
                l0= (x_alvo - pontos[j].x)/(pontos[i].x - pontos[j].x)
                l1 = (x_alvo - pontos[i].x)/(pontos[j].x - pontos[i].x)
                p = (l0*pontos[i].y)+(l1*pontos[j].y)
                valores.append(p)

    return valores


