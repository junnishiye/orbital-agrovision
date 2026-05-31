# Orbital AgroVision — Mission TerraGuard
# Data Structures and Algorithms
# Sistema com interface gráfica para monitoramento de missão espacial

import tkinter as tk
from tkinter import ttk, messagebox


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
        "status": "ESTÁVEL",
        "pontuacao": 0
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

    return {
        "ciclo": ciclo,
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao,
        "status": status,
        "pontuacao": pontuacao
    }


def inserir_leitura_manual():
    try:
        temperatura = float(entrada_temperatura.get())
        energia = float(entrada_energia.get())
        comunicacao = int(combo_comunicacao.get())

        if comunicacao not in [0, 1]:
            messagebox.showerror("Erro", "Comunicação deve ser 1 ou 0.")
            return

        leitura = criar_leitura(temperatura, energia, comunicacao)
        leituras.append(leitura)

        atualizar_tabela()
        limpar_campos()

        messagebox.showinfo(
            "Leitura cadastrada",
            f"Leitura adicionada com sucesso.\n"
            f"Status: {leitura['status']}\n"
            f"Pontuação: {leitura['pontuacao']}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos.")


def simular_leitura_automatica():
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

    atualizar_tabela()

    messagebox.showinfo(
        "Simulação automática",
        f"Leitura simulada adicionada.\n"
        f"Ciclo: {leitura['ciclo']}\n"
        f"Temperatura: {temperatura} °C\n"
        f"Energia: {energia}%\n"
        f"Comunicação: {comunicacao}\n"
        f"Status: {leitura['status']}"
    )


def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    for leitura in leituras:
        tabela.insert(
            "",
            "end",
            values=(
                leitura["ciclo"],
                leitura["temperatura"],
                leitura["energia"],
                leitura["comunicacao"],
                leitura["pontuacao"],
                leitura["status"]
            )
        )


def executar_analise():
    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, "ANÁLISE DAS LEITURAS\n")
    saida_texto.insert(tk.END, "-" * 60 + "\n")

    for leitura in leituras:
        alertas = analisar_leitura(leitura)

        saida_texto.insert(tk.END, f"Ciclo {leitura['ciclo']}\n")
        saida_texto.insert(tk.END, f"Status: {leitura['status']}\n")
        saida_texto.insert(tk.END, f"Pontuação de risco: {leitura['pontuacao']}\n")
        saida_texto.insert(tk.END, "Alertas:\n")

        for alerta in alertas:
            saida_texto.insert(tk.END, f"- {alerta}\n")

        saida_texto.insert(tk.END, "-" * 60 + "\n")


def ver_historico_alertas():
    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, "HISTÓRICO DE ALERTAS\n")
    saida_texto.insert(tk.END, "-" * 60 + "\n")

    encontrou_alerta = False

    for leitura in leituras:
        alertas = analisar_leitura(leitura)

        alertas_reais = [
            alerta for alerta in alertas
            if alerta != "Nenhum alerta. Operação estável."
        ]

        if alertas_reais:
            encontrou_alerta = True
            saida_texto.insert(
                tk.END,
                f"Ciclo {leitura['ciclo']} — {leitura['status']}\n"
            )

            for alerta in alertas_reais:
                saida_texto.insert(tk.END, f"- {alerta}\n")

            saida_texto.insert(tk.END, "-" * 60 + "\n")

    if not encontrou_alerta:
        saida_texto.insert(tk.END, "Nenhum alerta crítico registrado.\n")


def gerar_relatorio_resumido():
    saida_texto.delete("1.0", tk.END)

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

    saida_texto.insert(tk.END, "RELATÓRIO RESUMIDO DA MISSÃO\n")
    saida_texto.insert(tk.END, "-" * 60 + "\n")
    saida_texto.insert(tk.END, f"Total de leituras: {total_leituras}\n")
    saida_texto.insert(tk.END, f"Leituras estáveis: {total_estaveis}\n")
    saida_texto.insert(tk.END, f"Leituras em atenção: {total_atencao}\n")
    saida_texto.insert(tk.END, f"Leituras críticas: {total_criticos}\n")
    saida_texto.insert(tk.END, f"Ciclo mais crítico: {ciclo_mais_critico['ciclo']}\n")
    saida_texto.insert(tk.END, f"Maior pontuação de risco: {ciclo_mais_critico['pontuacao']}\n")

    if total_criticos > 0:
        conclusao = "A missão apresentou eventos críticos e exige ação imediata."
    elif total_atencao > 0:
        conclusao = "A missão exige acompanhamento preventivo."
    else:
        conclusao = "A missão está operando de forma estável."

    saida_texto.insert(tk.END, f"Conclusão: {conclusao}\n")


def limpar_campos():
    entrada_temperatura.delete(0, tk.END)
    entrada_energia.delete(0, tk.END)
    combo_comunicacao.set("1")


def encerrar_sistema():
    janela.destroy()


janela = tk.Tk()
janela.title("Orbital AgroVision — Data Structures")
janela.geometry("950x650")

titulo = tk.Label(
    janela,
    text="Orbital AgroVision — Mission TerraGuard",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

subtitulo = tk.Label(
    janela,
    text="Sistema de Monitoramento Operacional — Data Structures and Algorithms",
    font=("Arial", 11)
)
subtitulo.pack(pady=5)

frame_entrada = tk.LabelFrame(janela, text="Cadastro de leitura", padx=10, pady=10)
frame_entrada.pack(fill="x", padx=15, pady=10)

tk.Label(frame_entrada, text="Temperatura:").grid(row=0, column=0, padx=5, pady=5)
entrada_temperatura = tk.Entry(frame_entrada, width=15)
entrada_temperatura.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Energia (%):").grid(row=0, column=2, padx=5, pady=5)
entrada_energia = tk.Entry(frame_entrada, width=15)
entrada_energia.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_entrada, text="Comunicação:").grid(row=0, column=4, padx=5, pady=5)
combo_comunicacao = ttk.Combobox(frame_entrada, values=[1, 0], width=12)
combo_comunicacao.set("1")
combo_comunicacao.grid(row=0, column=5, padx=5, pady=5)

botao_inserir = tk.Button(
    frame_entrada,
    text="Inserir leitura manual",
    command=inserir_leitura_manual
)
botao_inserir.grid(row=0, column=6, padx=5, pady=5)

botao_simular = tk.Button(
    frame_entrada,
    text="Simular leitura automática",
    command=simular_leitura_automatica
)
botao_simular.grid(row=0, column=7, padx=5, pady=5)

frame_tabela = tk.LabelFrame(janela, text="Leituras cadastradas", padx=10, pady=10)
frame_tabela.pack(fill="both", expand=True, padx=15, pady=10)

colunas = ("ciclo", "temperatura", "energia", "comunicacao", "pontuacao", "status")

tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=8)

tabela.heading("ciclo", text="Ciclo")
tabela.heading("temperatura", text="Temperatura")
tabela.heading("energia", text="Energia")
tabela.heading("comunicacao", text="Comunicação")
tabela.heading("pontuacao", text="Pontuação")
tabela.heading("status", text="Status")

tabela.column("ciclo", width=80)
tabela.column("temperatura", width=120)
tabela.column("energia", width=100)
tabela.column("comunicacao", width=120)
tabela.column("pontuacao", width=100)
tabela.column("status", width=120)

tabela.pack(fill="both", expand=True)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(fill="x", padx=15, pady=5)

tk.Button(frame_botoes, text="Executar análise", command=executar_analise).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Histórico de alertas", command=ver_historico_alertas).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Gerar relatório", command=gerar_relatorio_resumido).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Encerrar", command=encerrar_sistema).pack(side="right", padx=5)

frame_saida = tk.LabelFrame(janela, text="Saída do sistema", padx=10, pady=10)
frame_saida.pack(fill="both", expand=True, padx=15, pady=10)

saida_texto = tk.Text(frame_saida, height=10)
saida_texto.pack(fill="both", expand=True)

atualizar_tabela()

janela.mainloop()