import matplotlib.pyplot as plt

def exibir_grafico(dados: list):
    dias = [d["dia"] for d in dados]
    maximas = [d["max"] for d in dados]
    minimas = [d["min"] for d in dados]
    medias = [d["media"] for d in dados]

    plt.figure(figsize=(10, 5))
    plt.plot(dias, maximas, label='Máximas', marker='o')
    plt.plot(dias, minimas, label='Mínimas', marker='o')
    plt.plot(dias, medias, label='Médias', marker='o')

    plt.title('Resumo Semanal de Temperatura')
    plt.xlabel('Dias da Semana')
    plt.ylabel('Temperatura (°C)')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()    

