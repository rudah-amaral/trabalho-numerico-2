from dataclasses import dataclass

#Vamos ter que criar um função para interpretar funções (já temos isso pronto)
#para ficar mais dinamico, só do hermes colocar o x_alvo e a função o nosso programa vai saber a imagem desejada
#lagrange funciona assim??? (não lembro direito)
#para não correr nenhum risco de perder valores importantes, a gnt vai precisar ser bem redundante
#amanhã eu vou fazer o neville

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


def neville(ponto: list[Ponto], x_alvo) -> list[float]:


def desvio_relativo_percentual(x_alvo, resultados: list[float]) -> list[float]:
    n = len(resultados)
    DRP = []

    for i in range(n):
        Desvio = abs((resultados[i] - x_alvo) / x_alvo)
        DRP.append(Desvio)

    return DRP



