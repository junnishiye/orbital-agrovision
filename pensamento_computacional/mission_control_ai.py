import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).parent.parent
sys.path.append(str(PASTA_RAIZ / "core_python"))

from leitor_dados import ler_dados_missao
from analisador_risco import analisar_missao
from relatorio_missao import gerar_relatorio


def carregar_matriz_dados():
    """
    Carrega os dados da missão e armazena na matriz dados_missao.
    Cada linha representa um ciclo da missão.
    Cada coluna representa uma variável monitorada.
    """

    dados_lidos = ler_dados_missao()

    dados_missao = []

    for ciclo in dados_lidos:
        linha = [
            ciclo["temperatura"],
            ciclo["comunicacao"],
            ciclo["bateria"],
            ciclo["oxigenio"],
            ciclo["estabilidade"],
            ciclo["luminosidade"],
            ciclo["vibracao"],
            ciclo["risco_ambiental"]
        ]

        dados_missao.append(linha)

    return dados_lidos, dados_missao


def exibir_cabecalho():
    print("=" * 70)
    print("ORBITAL AGROVISION — MISSION TERRAGUARD")
    print("Monitoramento Espacial Inteligente para Risco Ambiental Agrícola")
    print("=" * 70)


def exibir_matriz_dados(dados_missao):
    """
    Exibe a matriz dados_missao no terminal.
    """

    print("\nMATRIZ dados_missao")
    print("-" * 70)
    print("[temperatura, comunicacao, bateria, oxigenio, estabilidade, luminosidade, vibracao, risco_ambiental]")

    for indice, linha in enumerate(dados_missao, start=1):
        print(f"Ciclo {indice}: {linha}")


def exibir_ciclos(dados_lidos, resultados):
    print("\nANÁLISE DOS CICLOS DA MISSÃO")
    print("-" * 70)

    for ciclo, resultado in zip(dados_lidos, resultados):
        print(f"\nCICLO {ciclo['ciclo']}")
        print("-" * 70)

        print(f"Temperatura: {ciclo['temperatura']} °C")
        print(f"Comunicação: {ciclo['comunicacao']}%")
        print(f"Bateria: {ciclo['bateria']}%")
        print(f"Oxigênio: {ciclo['oxigenio']}%")
        print(f"Estabilidade: {ciclo['estabilidade']}%")
        print(f"Luminosidade: {ciclo['luminosidade']}")
        print(f"Vibração: {ciclo['vibracao']}")
        print(f"Risco ambiental: {ciclo['risco_ambiental']}")

        print(f"\nPontuação de risco: {resultado['pontuacao']}")
        print(f"Classificação: {resultado['classificacao']}")

        if resultado["alertas"]:
            print("Alertas:")
            for alerta in resultado["alertas"]:
                print(f"- {alerta}")
        else:
            print("Alertas: nenhum alerta registrado.")


def main():
    exibir_cabecalho()

    dados_lidos, dados_missao = carregar_matriz_dados()

    exibir_matriz_dados(dados_missao)

    resultados = analisar_missao(dados_lidos)

    exibir_ciclos(dados_lidos, resultados)

    print("\n")
    relatorio = gerar_relatorio(dados_lidos, resultados)
    print(relatorio)


if __name__ == "__main__":
    main()