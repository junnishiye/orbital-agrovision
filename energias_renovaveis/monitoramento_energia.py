# Orbital AgroVision — Mission TerraGuard
# Soluções em Energias Renováveis e Sustentáveis
# Monitoramento energético de missão espacial experimental

import sys
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


# Permite importar o leitor de dados da pasta core_python
PASTA_RAIZ = Path(__file__).parent.parent
sys.path.append(str(PASTA_RAIZ / "core_python"))

from leitor_dados import ler_dados_missao


dados_energia = []


def calcular_potencia_solar(luminosidade):
    """
    Simula a potência gerada por painéis solares.
    A luminosidade varia de 0 a 100.
    Para simplificar, cada ponto de luminosidade gera 5 W.
    """
    return luminosidade * 5


def calcular_consumo_estimado(temperatura, comunicacao, risco_ambiental):
    """
    Calcula um consumo energético estimado do módulo.
    O consumo aumenta em situações de temperatura elevada,
    comunicação ruim ou risco ambiental alto.
    """
    consumo_base = 280

    if temperatura > 35:
        consumo_base += 40

    if comunicacao < 60:
        consumo_base += 25

    if risco_ambiental > 70:
        consumo_base += 35

    return consumo_base


def gerar_alertas_energia(ciclo):
    """
    Gera alertas energéticos com base nos dados do ciclo.
    """
    alertas = []

    if ciclo["bateria"] < 20:
        alertas.append("Bateria crítica: ativar modo de economia de energia")
    elif ciclo["bateria"] < 50:
        alertas.append("Atenção: bateria abaixo do nível ideal")

    if ciclo["luminosidade"] < 40:
        alertas.append("Baixa luminosidade: geração solar reduzida")

    if ciclo["saldo_energetico"] < 0:
        alertas.append("Consumo maior que geração: risco de déficit energético")

    if ciclo["risco_ambiental"] > 70:
        alertas.append("Risco ambiental alto: priorizar funções críticas")

    if not alertas:
        alertas.append("Sistema energético estável")

    return alertas


def classificar_status_energetico(ciclo):
    """
    Classifica o estado energético do ciclo.
    """
    pontos = 0

    if ciclo["bateria"] < 20:
        pontos += 2
    elif ciclo["bateria"] < 50:
        pontos += 1

    if ciclo["luminosidade"] < 40:
        pontos += 1

    if ciclo["saldo_energetico"] < 0:
        pontos += 1

    if ciclo["risco_ambiental"] > 70:
        pontos += 1

    if pontos == 0:
        return "ESTÁVEL"
    elif pontos <= 2:
        return "ATENÇÃO"
    else:
        return "CRÍTICO"


def gerar_decisao_automatica(ciclo):
    """
    Define uma decisão automática para o módulo.
    """
    if ciclo["bateria"] < 20:
        return "Ativar economia de energia e desligar funções não essenciais"

    if ciclo["saldo_energetico"] < 0:
        return "Reduzir consumo e priorizar comunicação com a base"

    if ciclo["luminosidade"] < 40:
        return "Aguardar maior geração solar ou reduzir processamento"

    if ciclo["risco_ambiental"] > 70:
        return "Manter monitoramento ativo e priorizar sensores ambientais"

    return "Manter operação energética normal"


def carregar_dados_energeticos():
    """
    Carrega os dados da missão e cria uma estrutura específica
    para análise energética.
    """
    global dados_energia

    dados_missao = ler_dados_missao()
    dados_energia = []

    for ciclo in dados_missao:
        potencia_solar = calcular_potencia_solar(ciclo["luminosidade"])
        consumo_estimado = calcular_consumo_estimado(
            ciclo["temperatura"],
            ciclo["comunicacao"],
            ciclo["risco_ambiental"]
        )

        saldo_energetico = potencia_solar - consumo_estimado

        ciclo_energia = {
            "ciclo": ciclo["ciclo"],
            "temperatura": ciclo["temperatura"],
            "comunicacao": ciclo["comunicacao"],
            "bateria": ciclo["bateria"],
            "luminosidade": ciclo["luminosidade"],
            "risco_ambiental": ciclo["risco_ambiental"],
            "potencia_solar": potencia_solar,
            "consumo_estimado": consumo_estimado,
            "saldo_energetico": saldo_energetico,
        }

        ciclo_energia["status"] = classificar_status_energetico(ciclo_energia)
        ciclo_energia["decisao"] = gerar_decisao_automatica(ciclo_energia)
        ciclo_energia["alertas"] = gerar_alertas_energia(ciclo_energia)

        dados_energia.append(ciclo_energia)

    atualizar_tabela()
    messagebox.showinfo("Dados carregados", "Dados energéticos carregados com sucesso.")


def atualizar_tabela():
    """
    Atualiza a tabela da interface gráfica.
    """
    for item in tabela.get_children():
        tabela.delete(item)

    for ciclo in dados_energia:
        tabela.insert(
            "",
            "end",
            values=(
                ciclo["ciclo"],
                ciclo["bateria"],
                ciclo["luminosidade"],
                ciclo["potencia_solar"],
                ciclo["consumo_estimado"],
                ciclo["saldo_energetico"],
                ciclo["status"]
            )
        )


def exibir_alertas():
    """
    Exibe alertas energéticos por ciclo.
    """
    saida_texto.delete("1.0", tk.END)

    if not dados_energia:
        saida_texto.insert(tk.END, "Nenhum dado carregado.\n")
        return

    saida_texto.insert(tk.END, "ALERTAS ENERGÉTICOS — MISSION TERRAGUARD\n")
    saida_texto.insert(tk.END, "-" * 70 + "\n")

    for ciclo in dados_energia:
        saida_texto.insert(tk.END, f"Ciclo {ciclo['ciclo']} — {ciclo['status']}\n")
        saida_texto.insert(tk.END, f"Bateria: {ciclo['bateria']}%\n")
        saida_texto.insert(tk.END, f"Luminosidade: {ciclo['luminosidade']}\n")
        saida_texto.insert(tk.END, f"Potência solar simulada: {ciclo['potencia_solar']} W\n")
        saida_texto.insert(tk.END, f"Consumo estimado: {ciclo['consumo_estimado']} W\n")
        saida_texto.insert(tk.END, f"Saldo energético: {ciclo['saldo_energetico']} W\n")
        saida_texto.insert(tk.END, "Alertas:\n")

        for alerta in ciclo["alertas"]:
            saida_texto.insert(tk.END, f"- {alerta}\n")

        saida_texto.insert(tk.END, f"Decisão automática: {ciclo['decisao']}\n")
        saida_texto.insert(tk.END, "-" * 70 + "\n")


def gerar_relatorio_energetico():
    """
    Gera um relatório resumido da situação energética.
    """
    saida_texto.delete("1.0", tk.END)

    if not dados_energia:
        saida_texto.insert(tk.END, "Nenhum dado carregado.\n")
        return

    total_ciclos = len(dados_energia)
    media_bateria = sum(ciclo["bateria"] for ciclo in dados_energia) / total_ciclos
    media_potencia_solar = sum(ciclo["potencia_solar"] for ciclo in dados_energia) / total_ciclos
    media_consumo = sum(ciclo["consumo_estimado"] for ciclo in dados_energia) / total_ciclos

    ciclos_criticos = [
        ciclo for ciclo in dados_energia
        if ciclo["status"] == "CRÍTICO"
    ]

    ciclo_menor_bateria = min(dados_energia, key=lambda ciclo: ciclo["bateria"])
    ciclo_menor_luminosidade = min(dados_energia, key=lambda ciclo: ciclo["luminosidade"])

    saida_texto.insert(tk.END, "RELATÓRIO ENERGÉTICO — ORBITAL AGROVISION\n")
    saida_texto.insert(tk.END, "Missão: Mission TerraGuard\n")
    saida_texto.insert(tk.END, "-" * 70 + "\n")
    saida_texto.insert(tk.END, f"Total de ciclos analisados: {total_ciclos}\n")
    saida_texto.insert(tk.END, f"Média de bateria: {media_bateria:.2f}%\n")
    saida_texto.insert(tk.END, f"Média de potência solar simulada: {media_potencia_solar:.2f} W\n")
    saida_texto.insert(tk.END, f"Média de consumo estimado: {media_consumo:.2f} W\n")
    saida_texto.insert(tk.END, f"Quantidade de ciclos críticos: {len(ciclos_criticos)}\n")
    saida_texto.insert(tk.END, f"Ciclo com menor bateria: {ciclo_menor_bateria['ciclo']}\n")
    saida_texto.insert(tk.END, f"Ciclo com menor luminosidade: {ciclo_menor_luminosidade['ciclo']}\n")
    saida_texto.insert(tk.END, "-" * 70 + "\n")

    if ciclos_criticos:
        saida_texto.insert(
            tk.END,
            "Conclusão: a missão apresentou risco energético e exige economia de energia.\n"
        )
    else:
        saida_texto.insert(
            tk.END,
            "Conclusão: a missão manteve condição energética controlada.\n"
        )


def simular_modo_economia():
    """
    Simula o efeito do modo de economia de energia,
    reduzindo o consumo estimado em 20% nos ciclos críticos.
    """
    saida_texto.delete("1.0", tk.END)

    if not dados_energia:
        saida_texto.insert(tk.END, "Nenhum dado carregado.\n")
        return

    saida_texto.insert(tk.END, "SIMULAÇÃO DE MODO ECONOMIA DE ENERGIA\n")
    saida_texto.insert(tk.END, "-" * 70 + "\n")

    for ciclo in dados_energia:
        if ciclo["status"] == "CRÍTICO":
            consumo_original = ciclo["consumo_estimado"]
            consumo_reduzido = consumo_original * 0.8
            economia = consumo_original - consumo_reduzido

            saida_texto.insert(tk.END, f"Ciclo {ciclo['ciclo']}\n")
            saida_texto.insert(tk.END, f"Consumo original: {consumo_original:.2f} W\n")
            saida_texto.insert(tk.END, f"Consumo com economia: {consumo_reduzido:.2f} W\n")
            saida_texto.insert(tk.END, f"Economia estimada: {economia:.2f} W\n")
            saida_texto.insert(tk.END, "-" * 70 + "\n")


def encerrar():
    janela.destroy()


janela = tk.Tk()
janela.title("Orbital AgroVision — Energias Renováveis")
janela.geometry("1050x680")

titulo = tk.Label(
    janela,
    text="Orbital AgroVision — Mission TerraGuard",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

subtitulo = tk.Label(
    janela,
    text="Monitoramento Energético com Geração Solar Simulada",
    font=("Arial", 12)
)
subtitulo.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(fill="x", padx=15, pady=10)

tk.Button(
    frame_botoes,
    text="Carregar dados da missão",
    command=carregar_dados_energeticos
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Exibir alertas energéticos",
    command=exibir_alertas
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Gerar relatório energético",
    command=gerar_relatorio_energetico
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Simular modo economia",
    command=simular_modo_economia
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Encerrar",
    command=encerrar
).pack(side="right", padx=5)

frame_tabela = tk.LabelFrame(janela, text="Dados energéticos da missão", padx=10, pady=10)
frame_tabela.pack(fill="both", expand=True, padx=15, pady=10)

colunas = (
    "ciclo",
    "bateria",
    "luminosidade",
    "potencia_solar",
    "consumo",
    "saldo",
    "status"
)

tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

tabela.heading("ciclo", text="Ciclo")
tabela.heading("bateria", text="Bateria (%)")
tabela.heading("luminosidade", text="Luminosidade")
tabela.heading("potencia_solar", text="Potência solar (W)")
tabela.heading("consumo", text="Consumo (W)")
tabela.heading("saldo", text="Saldo (W)")
tabela.heading("status", text="Status")

tabela.column("ciclo", width=70)
tabela.column("bateria", width=100)
tabela.column("luminosidade", width=110)
tabela.column("potencia_solar", width=140)
tabela.column("consumo", width=120)
tabela.column("saldo", width=100)
tabela.column("status", width=110)

tabela.pack(fill="both", expand=True)

frame_saida = tk.LabelFrame(janela, text="Saída do sistema", padx=10, pady=10)
frame_saida.pack(fill="both", expand=True, padx=15, pady=10)

saida_texto = tk.Text(frame_saida, height=12)
saida_texto.pack(fill="both", expand=True)

janela.mainloop()
