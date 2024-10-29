import Pyro4
import numpy as np

# Conectando-se ao Name Server e buscando URIs específicos para cada função
ns = Pyro4.locateNS()
servers = {
    "media": Pyro4.Proxy(ns.lookup("data.analysis1")),
    "mediana": Pyro4.Proxy(ns.lookup("data.analysis2")),
    "media_ponderada": Pyro4.Proxy(ns.lookup("data.analysis3"))
}

# Função para tentar realizar a tarefa e redirecionar caso haja falha
def executar_tarefa(servidor, funcao, *args):
    try:
        return getattr(servidor, funcao)(*args)
    except Pyro4.errors.CommunicationError:
        print(f"Servidor para {funcao} falhou. Tentando outro servidor...")
        # Tenta encontrar outro servidor com a mesma função
        return None

# Definindo matrizes e pesos para as tarefas
matriz1 = np.random.randint(100, size=(5, 5)).tolist()
matriz2 = np.random.randint(100, size=(5, 5)).tolist()
pesos = [5, 2, 7, 0, 1]

# Distribuindo as tarefas para os servidores designados
resultado_media = executar_tarefa(servers["media"], "calcular_media", matriz1)
if resultado_media is None:
    print("Nenhum servidor disponível para calcular a média.")

resultado_mediana = executar_tarefa(servers["mediana"], "calcular_mediana", matriz2)
if resultado_mediana is None:
    print("Nenhum servidor disponível para calcular a mediana.")

resultado_media_ponderada = executar_tarefa(servers["media_ponderada"], "calcular_media_ponderada", matriz1, pesos)
if resultado_media_ponderada is None:
    print("Nenhum servidor disponível para calcular a média ponderada.")

# Exibindo os resultados
print("Resultados:")
print("Média:", resultado_media)
print("Mediana:", resultado_mediana)
print("Média Ponderada:", resultado_media_ponderada)
