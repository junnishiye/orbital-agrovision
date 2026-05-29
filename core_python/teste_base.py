from leitor_dados import ler_dados_missao
from analisador_risco import analisar_missao
from relatorio_missao import gerar_relatorio


def testar_leitura(dados):
    """
    Verifica se os dados foram carregados corretamente.
    """
    if not dados:
        print("ERRO: Nenhum dado foi carregado.")
        return False

    print("OK: Dados carregados com sucesso.")
    print(f"Quantidade de ciclos carregados: {len(dados)}")
    return True


def testar_analise(resultados):
    """
    Verifica se a análise de risco gerou resultados.
    """
    if not resultados:
        print("ERRO: Nenhum resultado de análise foi gerado.")
        return False

    print("OK: Análise de risco executada com sucesso.")
    return True


def testar_ciclo_critico(resultados):
    """
    Verifica se existe pelo menos um ciclo crítico.
    """
    ciclos_criticos = [
        resultado for resultado in resultados
        if resultado["classificacao"] == "CRÍTICO"
    ]

    if ciclos_criticos:
        print("OK: Pelo menos um ciclo crítico foi identificado.")
        for ciclo in ciclos_criticos:
            print(f"- Ciclo {ciclo['ciclo']} com pontuação {ciclo['pontuacao']}")
        return True

    print("ATENÇÃO: Nenhum ciclo crítico foi identificado.")
    return False


def main():
    print("=" * 60)
    print("TESTE BASE — ORBITAL AGROVISION")
    print("=" * 60)

    dados = ler_dados_missao()

    if not testar_leitura(dados):
        return

    resultados = analisar_missao(dados)

    if not testar_analise(resultados):
        return

    testar_ciclo_critico(resultados)

    print("-" * 60)
    print("RELATÓRIO GERADO PELO SISTEMA")
    print("-" * 60)

    relatorio = gerar_relatorio(dados, resultados)
    print(relatorio)


if __name__ == "__main__":
    main()
