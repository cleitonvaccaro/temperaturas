from coleta import obter_dados
from processamento import adicionar_media
from graficos import exibir_grafico

def main():
    dados = obter_dados()
    dados_processados = adicionar_media(dados)
    exibir_grafico(dados_processados)

if __name__ == "__main__":
    main()