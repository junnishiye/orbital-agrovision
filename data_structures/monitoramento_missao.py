# Orbital AgroVision — Mission TerraGuard
# Data Structures and Algorithms
# Sistema de monitoramento de missão espacial experimental

leituras = [
    {
        "ciclo": 1,
        "temperatura": 24,
        "energia": 88,
        "comunicacao": 1,
        "status": "ESTÁVEL",
        "pontuacao": 0
    },
    {
        "ciclo": 2,
        "temperatura": 38,
        "energia": 42,
        "comunicacao": 1,
        "status": "ATENÇÃO",
        "pontuacao": 1
    },
    {
        "ciclo": 3,
        "temperatura": 85,
        "energia": 18,
        "comunicacao": 0,
        "status": "CRÍTICO",
        "pontuacao": 6
    }
]


def exibir_menu():
    print("\n" + "=" * 60)
    print("ORBITAL AGROVISION — DATA STRUCTURES")
    print("Mission TerraGuard — Monitoramento Operacional")
    print("=" * 60)
    print("1 - Inserir nova leitura manual")
    print("2 - Simular leitura automática")
    print("3 - Visualizar leituras cadastradas")
    print("4 - Executar análise das leituras")
    print("5 - Ver histórico de alertas")
    print("6 - Gerar relatório resumido")
    print("7 - Encerrar sistema")


def calcular_pontuacao(temperatura, energia, comunicacao):
    pontuacao = 0

    if temperatura > 80:
        pontuacao += 2

    if energia < 20:
        pontuacao += 2

    if comunicacao == 0:
        pontuacao += 2

    return pontuacao


def classificar_status(pontuacao):
    if pontuacao == 0:
        return "ESTÁVEL"
    elif pontuacao <= 2:
        return "ATENÇÃO"
    else:
        return "CRÍTICO"


def analisar_leitura(leitura):
    alertas = []

    if leitura["temperatura"] > 80:
        alertas.append("Alerta de superaquecimento")

    if leitura["energia"] < 20:
        alertas.append("Economia de energia ativada")

    if leitura["comunicacao"] == 0:
        alertas.append("Falha de comunicação")

    if not alertas:
        alertas.append("Nenhum alerta. Operação estável.")

    return alertas


def criar_leitura(temperatura, energia, comunicacao):
    ciclo = len(leituras) + 1
    pontuacao = calcular_pontuacao(temperatura, energia, comunicacao)
    status = classificar_status(pontuacao)

    leitura = {
        "ciclo": ciclo,
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao,
        "status": status,
        "pontuacao": pontuacao
    }

    return leitura


def inserir_leitura_manual():
    print("\nINSERIR NOVA LEITURA MANUAL")
    print("-" * 60)

    try:
        temperatura = float(input("Temperatura da missão: "))
        energia = float(input("Nível de energia (%): "))
        comunicacao = int(input("Comunicação (1 = ativa / 0 = falha): "))

        if comunicacao not in [0, 1]:
            print("Valor inválido para comunicação. Use 1 para ativa ou 0 para falha.")
            return

        leitura = criar_leitura(temperatura, energia, comunicacao)
        leituras.append(leitura)

        print("Leitura cadastrada com sucesso.")
        print(f"Status calculado: {leitura['status']}")
        print(f"Pontuação de risco: {leitura['pontuacao']}")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")


def simular_leitura_automatica():
    print("\nSIMULAÇÃO AUTOMÁTICA DE SENSOR")
    print("-" * 60)

    cenarios_simulados = [
        [29, 76, 1],
        [45, 35, 1],
        [82, 55, 1],
        [91, 12, 0],
        [34, 18, 1],
        [67, 90, 0]
    ]

    indice = len(leituras) % len(cenarios_simulados)
    temperatura, energia, comunicacao = cenarios_simulados[indice]

    leitura = criar_leitura(temperatura, energia, comunicacao)
    leituras.append(leitura)

    print("Leitura automática simulada com sucesso.")
    print(f"Ciclo: {leitura['ciclo']}")
    print(f"Temperatura: {temperatura} °C")
    print(f"Energia: {energia}%")
    print(f"Comunicação: {comunicacao}")
    print(f"Status: {leitura['status']}")
    print(f"Pontuação de risco: {leitura['pontuacao']}")


def visualizar_leituras():
    print("\nLEITURAS CADASTRADAS")
    print("-" * 60)

    if not leituras:
        print("Nenhuma leitura cadastrada.")
        return

    for leitura in leituras:
        print(f"Ciclo {leitura['ciclo']}")
        print(f"Temperatura: {leitura['temperatura']} °C")
        print(f"Energia: {leitura['energia']}%")
        print(f"Comunicação: {leitura['comunicacao']}")
        print(f"Pontuação de risco: {leitura['pontuacao']}")
        print(f"Status: {leitura['status']}")
        print("-" * 60)


def executar_analise():
    print("\nANÁLISE DAS LEITURAS")
    print("-" * 60)

    if not leituras:
        print("Nenhuma leitura disponível para análise.")
        return

    for leitura in leituras:
        alertas = analisar_leitura(leitura)

        print(f"Ciclo {leitura['ciclo']}")
        print(f"Status: {leitura['status']}")
        print(f"Pontuação de risco: {leitura['pontuacao']}")
        print("Alertas:")

        for alerta in alertas:
            print(f"- {alerta}")

        print("-" * 60)


def ver_historico_alertas():
    print("\nHISTÓRICO DE ALERTAS")
    print("-" * 60)

    encontrou_alerta = False

    for leitura in leituras:
        alertas = analisar_leitura(leitura)
        alertas_reais = []

        for alerta in alertas:
            if alerta != "Nenhum alerta. Operação estável.":
                alertas_reais.append(alerta)

        if alertas_reais:
            encontrou_alerta = True
            print(f"Ciclo {leitura['ciclo']} — {leitura['status']}")
            for alerta in alertas_reais:
                print(f"- {alerta}")
            print("-" * 60)

    if not encontrou_alerta:
        print("Nenhum alerta crítico registrado.")


def gerar_relatorio_resumido():
    print("\nRELATÓRIO RESUMIDO DA MISSÃO")
    print("-" * 60)

    total_leituras = len(leituras)
    total_estaveis = 0
    total_atencao = 0
    total_criticos = 0

    ciclo_mais_critico = leituras[0]

    for leitura in leituras:
        if leitura["status"] == "ESTÁVEL":
            total_estaveis += 1
        elif leitura["status"] == "ATENÇÃO":
            total_atencao += 1
        elif leitura["status"] == "CRÍTICO":
            total_criticos += 1

        if leitura["pontuacao"] > ciclo_mais_critico["pontuacao"]:
            ciclo_mais_critico = leitura

    print(f"Total de leituras: {total_leituras}")
    print(f"Leituras estáveis: {total_estaveis}")
    print(f"Leituras em atenção: {total_atencao}")
    print(f"Leituras críticas: {total_criticos}")
    print(f"Ciclo mais crítico: {ciclo_mais_critico['ciclo']}")
    print(f"Maior pontuação de risco: {ciclo_mais_critico['pontuacao']}")

    if total_criticos > 0:
        print("Conclusão: a missão apresentou eventos críticos e exige ação imediata.")
    elif total_atencao > 0:
        print("Conclusão: a missão exige acompanhamento preventivo.")
    else:
        print("Conclusão: a missão está operando de forma estável.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_leitura_manual()
        elif opcao == "2":
            simular_leitura_automatica()
        elif opcao == "3":
            visualizar_leituras()
        elif opcao == "4":
            executar_analise()
        elif opcao == "5":
            ver_historico_alertas()
        elif opcao == "6":
            gerar_relatorio_resumido()
        elif opcao == "7":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()