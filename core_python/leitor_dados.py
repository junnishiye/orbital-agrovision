import csv
from pathlib import Path


def ler_dados_missao():
    """
    Lê o arquivo dados_missao_simulados.csv e retorna uma lista de ciclos da missão.
    Cada ciclo vira um dicionário com temperatura, comunicação, bateria etc.
    """

    # Caminho do arquivo CSV, saindo da pasta core_python e entrando em base_dados
    caminho_csv = Path(__file__).parent.parent / "base_dados" / "dados_missao_simulados.csv"

    dados_missao = []

    try:
        with open(caminho_csv, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                ciclo = {
                    "ciclo": int(linha["ciclo"]),
                    "temperatura": float(linha["temperatura"]),
                    "comunicacao": float(linha["comunicacao"]),
                    "bateria": float(linha["bateria"]),
                    "oxigenio": float(linha["oxigenio"]),
                    "estabilidade": float(linha["estabilidade"]),
                    "luminosidade": float(linha["luminosidade"]),
                    "vibracao": float(linha["vibracao"]),
                    "risco_ambiental": float(linha["risco_ambiental"]),
                }

                dados_missao.append(ciclo)

    except FileNotFoundError:
        print("Erro: arquivo dados_missao_simulados.csv não encontrado.")
    except KeyError as erro:
        print(f"Erro: coluna ausente no CSV: {erro}")
    except ValueError:
        print("Erro: algum valor do CSV não pôde ser convertido para número.")

    return dados_missao


def exibir_dados(dados_missao):
    """
    Mostra os dados lidos no terminal.
    """

    print("=" * 60)
    print("ORBITAL AGROVISION — DADOS DA MISSÃO")
    print("=" * 60)

    for ciclo in dados_missao:
        print(f"Ciclo {ciclo['ciclo']}")
        print(f"Temperatura: {ciclo['temperatura']} °C")
        print(f"Comunicação: {ciclo['comunicacao']}%")
        print(f"Bateria: {ciclo['bateria']}%")
        print(f"Oxigênio: {ciclo['oxigenio']}%")
        print(f"Estabilidade: {ciclo['estabilidade']}%")
        print(f"Luminosidade: {ciclo['luminosidade']}")
        print(f"Vibração: {ciclo['vibracao']}")
        print(f"Risco ambiental: {ciclo['risco_ambiental']}")
        print("-" * 60)


if __name__ == "__main__":
    dados = ler_dados_missao()
    exibir_dados(dados)
