def identificar_area_mais_afetada(dados_missao):
    """
    Soma a pontuação de risco de cada área monitorada
    e identifica qual foi a mais afetada durante a missão.
    """

    pontuacao_areas = {
        "Temperatura": 0,
        "Comunicação": 0,
        "Bateria": 0,
        "Oxigênio": 0,
        "Estabilidade": 0,
        "Vibração": 0,
        "Risco ambiental": 0
    }

    for ciclo in dados_missao:
        # Temperatura
        if ciclo["temperatura"] > 40:
            pontuacao_areas["Temperatura"] += 2
        elif ciclo["temperatura"] > 35:
            pontuacao_areas["Temperatura"] += 1

        # Comunicação
        if ciclo["comunicacao"] < 30:
            pontuacao_areas["Comunicação"] += 2
        elif ciclo["comunicacao"] < 60:
            pontuacao_areas["Comunicação"] += 1

        # Bateria
        if ciclo["bateria"] < 20:
            pontuacao_areas["Bateria"] += 2
        elif ciclo["bateria"] < 50:
            pontuacao_areas["Bateria"] += 1

        # Oxigênio
        if ciclo["oxigenio"] < 80:
            pontuacao_areas["Oxigênio"] += 2

        # Estabilidade
        if ciclo["estabilidade"] < 40:
            pontuacao_areas["Estabilidade"] += 2

        # Vibração
        if ciclo["vibracao"] > 60:
            pontuacao_areas["Vibração"] += 2

        # Risco ambiental
        if ciclo["risco_ambiental"] > 70:
            pontuacao_areas["Risco ambiental"] += 2

    area_mais_afetada = max(
        pontuacao_areas,
        key=pontuacao_areas.get
    )

    return area_mais_afetada, pontuacao_areas


def gerar_relatorio(dados_missao, resultados):
    """
    Gera um relatório final da missão com base nos dados e nas análises de risco.
    """

    if not dados_missao or not resultados:
        return "Nenhum dado disponível para gerar relatório."

    ciclo_mais_critico = max(
        resultados,
        key=lambda resultado: resultado["pontuacao"]
    )

    pontuacao_total = sum(
        resultado["pontuacao"] for resultado in resultados
    )

    risco_medio = pontuacao_total / len(resultados)

    ciclos_criticos = [
        resultado for resultado in resultados
        if resultado["classificacao"] == "CRÍTICO"
    ]

    primeira_pontuacao = resultados[0]["pontuacao"]
    ultima_pontuacao = resultados[-1]["pontuacao"]

    if ultima_pontuacao > primeira_pontuacao:
        tendencia = "A missão apresentou tendência de piora."
    elif ultima_pontuacao < primeira_pontuacao:
        tendencia = "A missão apresentou tendência de melhora."
    else:
        tendencia = "A missão permaneceu estável em relação ao início."

    area_mais_afetada, pontuacao_areas = identificar_area_mais_afetada(dados_missao)

    relatorio = []

    relatorio.append("=" * 70)
    relatorio.append("RELATÓRIO FINAL — ORBITAL AGROVISION")
    relatorio.append("Missão: Mission TerraGuard")
    relatorio.append("=" * 70)
    relatorio.append(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    relatorio.append(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico['ciclo']}")
    relatorio.append(f"Maior pontuação de risco: {ciclo_mais_critico['pontuacao']}")
    relatorio.append(f"Risco médio da missão: {risco_medio:.2f}")
    relatorio.append(f"Quantidade de ciclos críticos: {len(ciclos_criticos)}")
    relatorio.append(f"Tendência: {tendencia}")
    relatorio.append(f"Área mais afetada: {area_mais_afetada}")
    relatorio.append("-" * 70)

    relatorio.append("Pontuação acumulada por área:")
    for area, pontuacao in pontuacao_areas.items():
        relatorio.append(f"- {area}: {pontuacao} ponto(s)")

    relatorio.append("-" * 70)

    for resultado in resultados:
        relatorio.append(f"Ciclo {resultado['ciclo']} — {resultado['classificacao']}")
        relatorio.append(f"Pontuação de risco: {resultado['pontuacao']}")

        if resultado["alertas"]:
            relatorio.append("Alertas:")
            for alerta in resultado["alertas"]:
                relatorio.append(f"- {alerta}")
        else:
            relatorio.append("Nenhum alerta registrado.")

        relatorio.append("-" * 70)

    return "\n".join(relatorio)