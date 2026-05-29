# Orbital AgroVision — Mission TerraGuard
# Data Structures and Algorithms
# Sistema de monitoramento simples de missão espacial experimental

leituras = [
    {
        "temperatura": 24,
        "energia": 88,
        "comunicacao": 1,
        "status": "Operação normal"
    },
    {
        "temperatura": 85,
        "energia": 18,
        "comunicacao": 0,
        "status": "Risco operacional"
    }
]


def exibir_menu():
    print("\n" + "=" * 50)
    print("ORBITAL AGROVISION — DATA STRUCTURES")
    print("=" * 50)
    print("1 - Inserir nova leitura")
    print("2 - Visualizar leituras cadastradas")
    print("3 - Executar análise das leituras")
    print("4 - Ver histórico de alertas")
    print("5 - Encerrar sistema")


def inserir_leitura():
    print("\nINSERIR NOVA LEITURA")
    print("-" * 50)

    try:
        temperatura = float(input("Temperatura da missão: "))
        energia = float(input("Nível de energia (%): "))
        comunicacao = int(input("Comunicação (1 = ativa / 0 = falha): "))

        if comunicacao not in [0, 1]:
            print("Valor inválido para comunicação. Use 1 ou 0.")
            return

        if temperatura > 80 or energia < 20 or comunicacao == 0:
            status = "Risco operacional"
        else:
            status = "Operação normal"

        leitura = {
            "temperatura": temperatura,
            "energia": energia,
            "comunicacao": comunicacao,
            "status": status
        }

        leituras.append(leitura)
        print("Leitura cadastrada com sucesso.")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")


def visualizar_leituras():
    print("\nLEITURAS CADASTRADAS")
    print("-" * 50)

    if not leituras:
        print("Nenhuma leitura cadastrada.")
        return

    for indice, leitura in enumerate(leituras, start=1):
        print(f"Leitura {indice}")
        print(f"Temperatura: {leitura['temperatura']} °C")
        print(f"Energia: {leitura['energia']}%")
        print(f"Comunicação: {leitura['comunicacao']}")
        print(f"Status: {leitura['status']}")
        print("-" * 50)


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


def executar_analise():
    print("\nANÁLISE DAS LEITURAS")
    print("-" * 50)

    if not leituras:
        print("Nenhuma leitura disponível para análise.")
        return

    for indice, leitura in enumerate(leituras, start=1):
        alertas = analisar_leitura(leitura)

        print(f"Leitura {indice}")
        print(f"Status: {leitura['status']}")
        print("Alertas:")

        for alerta in alertas:
            print(f"- {alerta}")

        print("-" * 50)


def ver_historico_alertas():
    print("\nHISTÓRICO DE ALERTAS")
    print("-" * 50)

    encontrou_alerta = False

    for indice, leitura in enumerate(leituras, start=1):
        alertas = analisar_leitura(leitura)

        alertas_reais = [
            alerta for alerta in alertas
            if alerta != "Nenhum alerta. Operação estável."
        ]

        if alertas_reais:
            encontrou_alerta = True
            print(f"Leitura {indice}:")
            for alerta in alertas_reais:
                print(f"- {alerta}")
            print("-" * 50)

    if not encontrou_alerta:
        print("Nenhum alerta crítico registrado.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_leitura()
        elif opcao == "2":
            visualizar_leituras()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            ver_historico_alertas()
        elif opcao == "5":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
