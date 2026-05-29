from leitor_dados import ler_dados_missao


def analisar_ciclo(ciclo):
    """
    Analisa um ciclo da missão e retorna os alertas encontrados.
    """

    alertas = []
    pontuacao = 0

    # Temperatura
    if ciclo["temperatura"] > 40:
        alertas.append("Risco crítico ambiental por temperatura elevada")
        pontuacao += 2
    elif ciclo["temperatura"] > 35:
        alertas.append("Alerta de calor elevado")
        pontuacao += 1

    # Bateria
    if ciclo["bateria"] < 20:
        alertas.append("Bateria crítica: ativar economia de energia")
        pontuacao += 2
    elif ciclo["bateria"] < 50:
        alertas.append("Atenção energética: bateria abaixo do ideal")
        pontuacao += 1

    # Comunicação
    if ciclo["comunicacao"] < 30:
        alertas.append("Falha crítica de comunicação")
        pontuacao += 2
    elif ciclo["comunicacao"] < 60:
        alertas.append("Comunicação instável")
        pontuacao += 1

    # Oxigênio
    if ciclo["oxigenio"] < 80:
        alertas.append("Suporte operacional crítico")
        pontuacao += 2

    # Estabilidade
    if ciclo["estabilidade"] < 40:
        alertas.append("Instabilidade operacional crítica")
        pontuacao += 2

    # Vibração
    if ciclo["vibracao"] > 60:
        alertas.append("Possível impacto ou falha mecânica")
        pontuacao += 2

    # Risco ambiental
    if ciclo["risco_ambiental"] > 70:
        alertas.append("Área agrícola em risco ambiental alto")
        pontuacao += 2

    # Classificação geral do ciclo
    if pontuacao <= 2:
        classificacao = "ESTÁVEL"
    elif pontuacao <= 5:
        classificacao = "ATENÇÃO"
    else:
        classificacao = "CRÍTICO"

    return {
        "ciclo": ciclo["ciclo"],
        "pontuacao": pontuacao,
        "classificacao": classificacao,
        "alertas": alertas
    }


def analisar_missao(dados_missao):
    """
    Analisa todos os ciclos da missão.
    """

    resultados = []

    for ciclo in dados_missao:
        resultado = analisar_ciclo(ciclo)
        resultados.append(resultado)

    return resultados


def exibir_resultados(resultados):
    """
    Mostra os resultados da análise no terminal.
    """

    print("=" * 60)
    print("ORBITAL AGROVISION — ANÁLISE DE RISCO")
    print("=" * 60)

    for resultado in resultados:
        print(f"Ciclo {resultado['ciclo']}")
        print(f"Pontuação de risco: {resultado['pontuacao']}")
        print(f"Classificação: {resultado['classificacao']}")

        if resultado["alertas"]:
            print("Alertas:")
            for alerta in resultado["alertas"]:
                print(f"- {alerta}")
        else:
            print("Nenhum alerta encontrado.")

        print("-" * 60)


if __name__ == "__main__":
    dados = ler_dados_missao()
    resultados = analisar_missao(dados)
    exibir_resultados(resultados)
