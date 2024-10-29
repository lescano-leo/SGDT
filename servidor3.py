import Pyro4
import numpy as np

@Pyro4.expose
class CalculoMediaPonderada:
    # def calcular_media (self, matriz):
    #     matriz = np.array(matriz)
    #     return float(np.mean(matriz))
    # def calcular_mediana(self, matriz):
    #     matriz = np.array(matriz)
    #     return float(np.median(matriz))  # Retorna mediana como float simples

    def calcular_media_ponderada(self, matriz, pesos):
        matriz = np.array(matriz)
        pesos = np.array(pesos)
        media_ponderada = np.average(matriz, axis=1, weights=pesos)
        return media_ponderada.tolist()  # Retorna como lista para serialização

# Configurando o servidor
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(CalculoMediaPonderada)
ns.register("data.analysis3", uri)
print("Servidor pronto para receber tarefas.")
daemon.requestLoop()