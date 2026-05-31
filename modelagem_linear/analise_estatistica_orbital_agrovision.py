# -*- coding: utf-8 -*-
"""
GLOBAL SOLUTION 2026.1 - ORBITAL AGROVISION / MISSION TERRAGUARD
Disciplina: Modelagem Linear para Aprendizado de Maquina
Tema: Analise estatistica de dados espaciais reais como apoio ao monitoramento ambiental agricola

Integrantes:
- Davi Sinhorini Pacheco - RM 569487
- Joao Vitor Jun Nishiye De Sousa - RM 572079


"""

from __future__ import annotations

import fnmatch
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# CONFIGURACOES GERAIS
# =========================================================

NOME_BASE_PRINCIPAL = "base_real.csv"
PADROES_BASE_ACEITOS = ["base_real.csv", "base_real*.csv"]

# Por seguranca e desempenho, o codigo procura dentro da pasta do script,
# pasta atual, Downloads, Documentos, Area de Trabalho e pasta do usuario.
# Se quiser procurar no sistema inteiro, mude para True.
BUSCAR_SISTEMA_INTEIRO = False

MOSTRAR_GRAFICOS_NA_TELA = True

PASTA_RESULTADOS = Path("resultados_orbital_agrovision")
PASTA_GRAFICOS = PASTA_RESULTADOS / "graficos"
PASTA_TABELAS = PASTA_RESULTADOS / "tabelas"

PASTAS_IGNORADAS = {
    ".cache",
    ".config",
    ".local",
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "Trash",
    "lixeira",
}


# =========================================================
# FUNCOES DE BUSCA DO ARQUIVO
# =========================================================

def obter_pasta_script() -> Path:
    """Retorna a pasta onde o script esta salvo."""
    try:
        return Path(__file__).resolve().parent
    except NameError:
        return Path.cwd().resolve()


def arquivo_bate_com_padrao(nome_arquivo: str) -> bool:
    """Verifica se o nome do arquivo parece ser a base esperada."""
    return any(fnmatch.fnmatch(nome_arquivo, padrao) for padrao in PADROES_BASE_ACEITOS)


def buscar_arquivo_recursivo(raiz: Path) -> list[Path]:
    """Busca arquivos base_real*.csv dentro de uma pasta, ignorando pastas pesadas."""
    encontrados: list[Path] = []

    if not raiz.exists() or not raiz.is_dir():
        return encontrados

    try:
        for pasta_atual, subpastas, arquivos in os.walk(raiz):
            # Evita pastas muito grandes, escondidas ou irrelevantes para este projeto.
            subpastas[:] = [
                pasta for pasta in subpastas
                if pasta not in PASTAS_IGNORADAS and not pasta.startswith(".")
            ]

            for arquivo in arquivos:
                if arquivo_bate_com_padrao(arquivo):
                    encontrados.append(Path(pasta_atual) / arquivo)

    except PermissionError:
        pass

    return encontrados


def montar_pastas_de_busca() -> list[Path]:
    """Monta uma lista de pastas provaveis para procurar a base."""
    pasta_script = obter_pasta_script()
    pasta_atual = Path.cwd().resolve()
    home = Path.home().resolve()

    pastas = [
        pasta_script,
        pasta_atual,
        home / "Downloads",
        home / "Documentos",
        home / "Documents",
        home / "Area de Trabalho",
        home / "Desktop",
        home / "gs",
        home,
    ]

    if BUSCAR_SISTEMA_INTEIRO:
        pastas.append(Path("/"))

    # Remove repetidas mantendo a ordem.
    pastas_unicas = []
    vistas = set()

    for pasta in pastas:
        try:
            pasta_resolvida = pasta.resolve()
        except FileNotFoundError:
            continue

        if pasta_resolvida not in vistas:
            vistas.add(pasta_resolvida)
            pastas_unicas.append(pasta_resolvida)

    return pastas_unicas


def escolher_melhor_arquivo(candidatos: list[Path]) -> Path:
    """Escolhe o melhor arquivo encontrado, priorizando base_real.csv exato e mais recente."""
    if not candidatos:
        raise FileNotFoundError("Nenhum arquivo candidato foi encontrado.")

    candidatos_existentes = [p for p in candidatos if p.exists() and p.is_file()]

    exatos = [p for p in candidatos_existentes if p.name == NOME_BASE_PRINCIPAL]
    grupo = exatos if exatos else candidatos_existentes

    return max(grupo, key=lambda p: p.stat().st_mtime)


def encontrar_base() -> Path:
    """
    Encontra a base real do projeto.

    Formas aceitas:
    1. Passar o caminho no terminal:
       python analise.py /caminho/para/base_real.csv
    2. Deixar o arquivo como base_real.csv em alguma pasta comum.
    3. Deixar como base_real(1).csv, base_real(2).csv etc.
    """
    # Caso o usuario passe o caminho manualmente no terminal.
    if len(sys.argv) > 1:
        caminho_manual = Path(sys.argv[1]).expanduser().resolve()
        if caminho_manual.exists() and caminho_manual.is_file():
            print(f"Base informada manualmente: {caminho_manual}")
            return caminho_manual
        raise FileNotFoundError(f"O caminho informado nao existe: {caminho_manual}")

    candidatos: list[Path] = []

    for pasta in montar_pastas_de_busca():
        encontrados = buscar_arquivo_recursivo(pasta)
        candidatos.extend(encontrados)

        # Se achou base_real.csv exato cedo, ja pode parar.
        if any(p.name == NOME_BASE_PRINCIPAL for p in encontrados):
            break

    # Remove duplicados.
    candidatos_unicos = sorted(set(candidatos))

    if not candidatos_unicos:
        raise FileNotFoundError(
            "Nao encontrei a base. Renomeie o arquivo para base_real.csv "
            "ou execute o codigo passando o caminho manualmente."
        )

    escolhido = escolher_melhor_arquivo(candidatos_unicos)

    print("\nArquivos de base encontrados:")
    for candidato in candidatos_unicos[:10]:
        print(f"- {candidato}")

    if len(candidatos_unicos) > 10:
        print(f"... e mais {len(candidatos_unicos) - 10} arquivo(s).")

    print(f"\nBase escolhida para a analise: {escolhido}\n")
    return escolhido


# =========================================================
# PREPARACAO DA BASE
# =========================================================

def carregar_e_tratar_base(caminho_base: Path) -> pd.DataFrame:
    """Carrega, padroniza e limpa a base Meteorite Landings."""
    df = pd.read_csv(caminho_base)

    print("Colunas encontradas na base original:")
    print(df.columns.tolist())

    # Padroniza espacos nos nomes das colunas.
    df.columns = df.columns.str.strip()

    # A coluna de massa pode variar dependendo da fonte/exportacao.
    if "mass (g)" in df.columns:
        df = df.rename(columns={"mass (g)": "mass_g"})
    elif "mass" in df.columns:
        df = df.rename(columns={"mass": "mass_g"})

    colunas_obrigatorias = {"year", "mass_g"}
    colunas_faltando = colunas_obrigatorias - set(df.columns)

    if colunas_faltando:
        raise ValueError(
            "A base precisa conter as colunas year e mass_g. "
            f"Colunas faltando: {colunas_faltando}. "
            f"Colunas encontradas: {df.columns.tolist()}"
        )

    # Converte ano, aceitando formatos como 2003, 2003-01-01 ou texto com ano.
    df["year"] = df["year"].astype(str).str.extract(r"(\d{4})")[0]
    df["year"] = pd.to_numeric(df["year"], errors="coerce")

    # Converte massa para numero.
    df["mass_g"] = pd.to_numeric(df["mass_g"], errors="coerce")

    # Remove registros invalidos.
    df = df.dropna(subset=["year", "mass_g"])
    df = df[(df["year"] >= 1800) & (df["year"] <= 2026)]
    df = df[df["mass_g"] > 0]

    # Cria decada.
    df["year"] = df["year"].astype(int)
    df["decade"] = (df["year"] // 10 * 10).astype(int)

    # Algo a mais: classificacao por quartis da massa.
    q1 = df["mass_g"].quantile(0.25)
    q3 = df["mass_g"].quantile(0.75)
    limite_outlier = q3 + 1.5 * (q3 - q1)

    def classificar_massa(massa: float) -> str:
        if massa > limite_outlier:
            return "evento_extremo"
        if massa >= q3:
            return "massa_alta"
        if massa >= q1:
            return "massa_media"
        return "massa_baixa"

    df["classificacao_massa"] = df["mass_g"].apply(classificar_massa)

    # Escala logaritmica para evitar distorcao visual causada por valores extremos.
    df["log10_mass_g"] = np.log10(df["mass_g"])

    print("\nBase tratada com sucesso.")
    print(f"Registros validos: {len(df):,}".replace(",", "."))
    print(df[["year", "decade", "mass_g", "log10_mass_g", "classificacao_massa"]].head())

    return df


# =========================================================
# TABELAS DE FREQUENCIA
# =========================================================

def gerar_tabela_frequencia_discreta(df: pd.DataFrame) -> pd.DataFrame:
    """Gera tabela de frequencia para variavel quantitativa discreta: decada."""
    freq = (
        df["decade"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    freq.columns = ["decada", "frequencia"]
    freq["frequencia_relativa_%"] = (freq["frequencia"] / freq["frequencia"].sum() * 100).round(2)
    freq["frequencia_acumulada"] = freq["frequencia"].cumsum()

    return freq


def gerar_tabela_frequencia_continua(df: pd.DataFrame) -> pd.DataFrame:
    """Gera tabela de frequencia para variavel quantitativa continua: massa em escala log10."""
    serie_log = df["log10_mass_g"]

    bins = np.linspace(serie_log.min(), serie_log.max(), 9)
    categorias = pd.cut(serie_log, bins=bins, include_lowest=True)

    freq = (
        categorias
        .value_counts()
        .sort_index()
        .reset_index()
    )

    freq.columns = ["classe_log10_massa_g", "frequencia"]
    freq["classe_log10_massa_g"] = freq["classe_log10_massa_g"].astype(str)
    freq["frequencia_relativa_%"] = (freq["frequencia"] / freq["frequencia"].sum() * 100).round(2)
    freq["frequencia_acumulada"] = freq["frequencia"].cumsum()

    return freq


# =========================================================
# ESTATISTICA DESCRITIVA
# =========================================================

def estatistica_descritiva(serie: pd.Series, nome_variavel: str) -> dict[str, float | str]:
    """Calcula medidas descritivas principais para uma serie numerica."""
    moda = serie.mode()
    moda_valor = moda.iloc[0] if not moda.empty else np.nan

    media = serie.mean()
    desvio_padrao = serie.std()
    coef_variacao = (desvio_padrao / media) * 100 if media != 0 else np.nan

    return {
        "variavel": nome_variavel,
        "media": round(media, 2),
        "mediana": round(serie.median(), 2),
        "moda": round(moda_valor, 2),
        "maximo": round(serie.max(), 2),
        "minimo": round(serie.min(), 2),
        "amplitude": round(serie.max() - serie.min(), 2),
        "variancia": round(serie.var(), 2),
        "desvio_padrao": round(desvio_padrao, 2),
        "coeficiente_variacao_%": round(coef_variacao, 2),
        "Q1": round(serie.quantile(0.25), 2),
        "Q2": round(serie.quantile(0.50), 2),
        "Q3": round(serie.quantile(0.75), 2),
    }


def gerar_estatisticas(df: pd.DataFrame) -> pd.DataFrame:
    """Gera estatistica descritiva para massa e ano."""
    resultados = [
        estatistica_descritiva(df["mass_g"], "massa_g"),
        estatistica_descritiva(df["year"], "ano"),
    ]

    return pd.DataFrame(resultados)


# =========================================================
# GRAFICOS
# =========================================================

def gerar_grafico_meteoritos_por_decada(df: pd.DataFrame) -> None:
    """Gera e salva grafico de barras com quantidade de meteoritos por decada."""
    por_decada = df.groupby("decade").size()

    plt.figure(figsize=(12, 5))
    por_decada.plot(kind="bar", color="steelblue")

    plt.title("Quantidade de meteoritos registrados por decada")
    plt.xlabel("Decada")
    plt.ylabel("Quantidade de registros")
    plt.xticks(rotation=45)
    plt.tight_layout()

    caminho = PASTA_GRAFICOS / "grafico_meteoritos_por_decada.png"
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    if MOSTRAR_GRAFICOS_NA_TELA:
        plt.show()

    plt.close()
    print(f"Grafico salvo: {caminho}")


def gerar_grafico_distribuicao_massa(df: pd.DataFrame) -> None:
    """Gera e salva histograma da massa em escala log10."""
    plt.figure(figsize=(9, 5))
    plt.hist(df["log10_mass_g"], bins=30, color="darkorange", edgecolor="black")

    plt.title("Distribuicao da massa dos meteoritos em escala log10")
    plt.xlabel("log10(massa em gramas)")
    plt.ylabel("Frequencia")
    plt.tight_layout()

    caminho = PASTA_GRAFICOS / "grafico_distribuicao_massa.png"
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    if MOSTRAR_GRAFICOS_NA_TELA:
        plt.show()

    plt.close()
    print(f"Grafico salvo: {caminho}")


def gerar_grafico_classificacao_massa(df: pd.DataFrame) -> None:
    """Algo a mais: grafico da classificacao dos meteoritos por criticidade de massa."""
    ordem = ["massa_baixa", "massa_media", "massa_alta", "evento_extremo"]
    contagem = df["classificacao_massa"].value_counts().reindex(ordem, fill_value=0)

    plt.figure(figsize=(9, 5))
    contagem.plot(kind="bar", color="seagreen")

    plt.title("Classificacao dos meteoritos por faixa de massa")
    plt.xlabel("Classificacao")
    plt.ylabel("Quantidade de registros")
    plt.xticks(rotation=20)
    plt.tight_layout()

    caminho = PASTA_GRAFICOS / "grafico_classificacao_massa.png"
    plt.savefig(caminho, dpi=300, bbox_inches="tight")

    if MOSTRAR_GRAFICOS_NA_TELA:
        plt.show()

    plt.close()
    print(f"Grafico salvo: {caminho}")


def gerar_graficos(df: pd.DataFrame) -> None:
    """Gera todos os graficos da analise."""
    gerar_grafico_meteoritos_por_decada(df)
    gerar_grafico_distribuicao_massa(df)
    gerar_grafico_classificacao_massa(df)


# =========================================================
# EXPORTACOES
# =========================================================

def criar_pastas_resultado() -> None:
    """Cria pastas de resultado caso nao existam."""
    PASTA_RESULTADOS.mkdir(exist_ok=True)
    PASTA_GRAFICOS.mkdir(exist_ok=True)
    PASTA_TABELAS.mkdir(exist_ok=True)


def gerar_resumo_txt(
    df: pd.DataFrame,
    freq_discreta: pd.DataFrame,
    freq_continua: pd.DataFrame,
    estatisticas: pd.DataFrame,
) -> None:
    """Gera um arquivo TXT com resumo interpretativo para apoiar o relatorio."""
    decada_maior = freq_discreta.loc[freq_discreta["frequencia"].idxmax(), "decada"]
    freq_decada_maior = freq_discreta["frequencia"].max()

    massa_media = estatisticas.loc[estatisticas["variavel"] == "massa_g", "media"].iloc[0]
    massa_mediana = estatisticas.loc[estatisticas["variavel"] == "massa_g", "mediana"].iloc[0]

    qtd_extremos = (df["classificacao_massa"] == "evento_extremo").sum()
    percentual_extremos = qtd_extremos / len(df) * 100

    texto = f"""ORBITAL AGROVISION - MISSION TERRAGUARD
Resumo automatico da analise estatistica

Base analisada: Meteorite Landings - NASA/Data.gov
Registros validos apos limpeza: {len(df)}
Periodo analisado: {df['year'].min()} a {df['year'].max()}

1. Frequencia discreta
A decada com maior numero de registros foi {decada_maior}, com {freq_decada_maior} ocorrencias.
Isso indica concentracao temporal dos registros, provavelmente associada ao avanco da catalogacao cientifica.

2. Frequencia continua
A massa foi analisada em escala log10 porque ha grande diferenca entre meteoritos pequenos e meteoritos extremamente pesados.
Essa transformacao reduz distorcoes visuais e melhora a interpretacao estatistica.

3. Estatistica descritiva
Media da massa: {massa_media} g
Mediana da massa: {massa_mediana} g
A media ser muito maior que a mediana indica assimetria positiva, causada por poucos meteoritos de massa extremamente elevada.

4. Algo a mais: eventos extremos
Foram identificados {qtd_extremos} registros classificados como evento_extremo, equivalentes a {percentual_extremos:.2f}% da base tratada.
No contexto da Mission TerraGuard, essa logica reforca a importancia de detectar anomalias e eventos criticos, como calor elevado, falha energetica, comunicacao instavel e risco ambiental alto em areas agricolas.

5. Conexao com a Orbital AgroVision
A base real de meteoritos e usada para treinar a leitura estatistica de dados espaciais e eventos extremos.
A aplicacao agricola aparece na interpretacao dos riscos e na integracao com a Orbital AgroVision, que transforma dados monitorados em alertas e decisoes sustentaveis para o agronegocio.
"""

    caminho = PASTA_RESULTADOS / "resumo_interpretativo.txt"
    caminho.write_text(texto, encoding="utf-8")
    print(f"Resumo interpretativo salvo: {caminho}")


def exportar_resultados(
    df: pd.DataFrame,
    freq_discreta: pd.DataFrame,
    freq_continua: pd.DataFrame,
    estatisticas: pd.DataFrame,
) -> None:
    """Exporta tabelas e arquivos finais."""
    df.to_csv(PASTA_TABELAS / "base_tratada.csv", index=False)
    freq_discreta.to_csv(PASTA_TABELAS / "frequencia_discreta_decadas.csv", index=False)
    freq_continua.to_csv(PASTA_TABELAS / "frequencia_continua_massa.csv", index=False)
    estatisticas.to_csv(PASTA_TABELAS / "estatistica_descritiva.csv", index=False)

    top_10 = df.sort_values("mass_g", ascending=False).head(10)
    top_10.to_csv(PASTA_TABELAS / "top_10_meteoritos_maior_massa.csv", index=False)

    gerar_resumo_txt(df, freq_discreta, freq_continua, estatisticas)

    print("\nArquivos exportados com sucesso na pasta resultados_orbital_agrovision.")


# =========================================================
# EXECUCAO PRINCIPAL
# =========================================================

def main() -> None:
    criar_pastas_resultado()

    caminho_base = encontrar_base()
    df = carregar_e_tratar_base(caminho_base)

    freq_discreta = gerar_tabela_frequencia_discreta(df)
    freq_continua = gerar_tabela_frequencia_continua(df)
    estatisticas = gerar_estatisticas(df)

    print("\nTabela de frequencia - variavel discreta: decada")
    print(freq_discreta)

    print("\nTabela de frequencia - variavel continua: log10 massa")
    print(freq_continua)

    print("\nEstatistica descritiva")
    print(estatisticas)

    gerar_graficos(df)
    exportar_resultados(df, freq_discreta, freq_continua, estatisticas)

    print("\nAnalise finalizada.")
    print(f"Veja os resultados em: {PASTA_RESULTADOS.resolve()}")


if __name__ == "__main__":
    main()
