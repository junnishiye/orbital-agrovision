# Explicação da Lógica — Data Structures and Algorithms

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este sistema simula o monitoramento operacional de uma missão espacial experimental aplicada ao contexto da Orbital AgroVision.

A proposta é acompanhar informações básicas da missão, como temperatura, energia e comunicação, utilizando estruturas de dados, funções, condicionais e repetição para identificar situações de risco e organizar as leituras no terminal.

---

## Objetivo do sistema

O objetivo do programa é permitir que o usuário monitore dados simulados da missão por meio de um menu interativo.

O sistema permite:

* Inserir uma nova leitura manual;
* Simular uma leitura automática;
* Visualizar leituras cadastradas;
* Executar análise automática das leituras;
* Consultar histórico de alertas;
* Gerar relatório resumido da missão;
* Encerrar o sistema.

---

## Dados monitorados

Cada leitura da missão possui as seguintes informações:

| Dado          | Descrição                                                      |
| ------------- | -------------------------------------------------------------- |
| `ciclo`       | Identificação sequencial da leitura                            |
| `temperatura` | Temperatura registrada na missão                               |
| `energia`     | Nível de energia disponível                                    |
| `comunicacao` | Estado da comunicação, sendo 1 para ativa e 0 para falha       |
| `status`      | Classificação geral da leitura                                 |
| `pontuacao`   | Pontuação de risco calculada a partir das condições analisadas |

---

## Estrutura de dados utilizada

O sistema utiliza uma lista chamada `leituras`.

Essa lista armazena várias leituras da missão. Cada leitura é representada por um dicionário contendo ciclo, temperatura, energia, comunicação, status e pontuação de risco.

Exemplo:

```python
leituras = [
    {
        "ciclo": 1,
        "temperatura": 24,
        "energia": 88,
        "comunicacao": 1,
        "status": "ESTÁVEL",
        "pontuacao": 0
    }
]
```

A lista funciona como um histórico das leituras registradas durante a execução do programa.

O uso de dicionários permite organizar cada leitura com nomes claros para os dados, facilitando a análise e a exibição das informações.

---

## Menu interativo

O sistema possui um menu com sete opções:

```text
1 - Inserir nova leitura manual
2 - Simular leitura automática
3 - Visualizar leituras cadastradas
4 - Executar análise das leituras
5 - Ver histórico de alertas
6 - Gerar relatório resumido
7 - Encerrar sistema
```

O menu é controlado por uma estrutura de repetição `while True`, mantendo o sistema em execução até que o usuário escolha a opção de encerramento.

---

## Funções utilizadas

O código foi dividido em funções para melhorar a organização e facilitar a manutenção.

| Função                         | Finalidade                                            |
| ------------------------------ | ----------------------------------------------------- |
| `exibir_menu()`                | Mostra o menu principal                               |
| `calcular_pontuacao()`         | Calcula a pontuação de risco de uma leitura           |
| `classificar_status()`         | Classifica a leitura como estável, atenção ou crítico |
| `analisar_leitura()`           | Verifica as condições de risco e gera alertas         |
| `criar_leitura()`              | Cria uma nova leitura com ciclo, status e pontuação   |
| `inserir_leitura_manual()`     | Permite cadastrar uma nova leitura manualmente        |
| `simular_leitura_automatica()` | Gera uma leitura simulada automaticamente             |
| `visualizar_leituras()`        | Exibe todas as leituras cadastradas                   |
| `executar_analise()`           | Analisa todas as leituras e exibe os alertas          |
| `ver_historico_alertas()`      | Mostra apenas os ciclos que possuem alertas reais     |
| `gerar_relatorio_resumido()`   | Gera um resumo geral da missão                        |
| `main()`                       | Controla o fluxo principal do programa                |

---

## Regras de análise

O sistema utiliza as regras principais exigidas na atividade:

| Condição         | Resposta do sistema         |
| ---------------- | --------------------------- |
| Temperatura > 80 | Alerta de superaquecimento  |
| Energia < 20     | Economia de energia ativada |
| Comunicação = 0  | Falha de comunicação        |

Essas regras são aplicadas durante a análise das leituras.

---

## Pontuação de risco

Cada condição crítica aumenta a pontuação de risco da leitura.

| Condição         | Pontuação |
| ---------------- | --------: |
| Temperatura > 80 | +2 pontos |
| Energia < 20     | +2 pontos |
| Comunicação = 0  | +2 pontos |

A pontuação é calculada na função `calcular_pontuacao()`.

Exemplo:

```python
if temperatura > 80:
    pontuacao += 2

if energia < 20:
    pontuacao += 2

if comunicacao == 0:
    pontuacao += 2
```

---

## Classificação do status

Após calcular a pontuação, o sistema classifica a leitura.

|  Pontuação | Status  |
| ---------: | ------- |
|          0 | ESTÁVEL |
|      1 a 2 | ATENÇÃO |
| Acima de 2 | CRÍTICO |

Essa lógica é aplicada na função `classificar_status()`.

---

## Inserção manual de leitura

Na opção 1, o usuário informa manualmente:

* Temperatura;
* Nível de energia;
* Comunicação.

Depois disso, o sistema calcula automaticamente a pontuação, classifica o status e armazena a leitura na lista `leituras`.

---

## Simulação automática de leitura

Na opção 2, o sistema gera uma leitura simulada a partir de cenários previamente definidos.

Essa funcionalidade representa a entrada automática de dados por sensores simulados, mantendo a proposta de monitoramento de uma missão espacial experimental.

---

## Visualização das leituras

Na opção 3, o sistema percorre a lista `leituras` e exibe todos os dados cadastrados.

São mostrados:

* Ciclo;
* Temperatura;
* Energia;
* Comunicação;
* Pontuação de risco;
* Status.

Essa etapa demonstra o uso de repetição para percorrer uma estrutura de dados.

---

## Análise automática

Na opção 4, o sistema percorre todas as leituras e aplica as regras de alerta.

Exemplo:

```python
if leitura["temperatura"] > 80:
    alertas.append("Alerta de superaquecimento")
```

Se uma condição for verdadeira, o alerta correspondente é adicionado à lista de alertas.

---

## Histórico de alertas

Na opção 5, o sistema mostra apenas os ciclos que possuem alertas reais.

Isso permite visualizar rapidamente quais leituras apresentaram risco durante a missão, sem exibir leituras estáveis.

---

## Relatório resumido

Na opção 6, o sistema gera um relatório resumido da missão.

O relatório apresenta:

* Total de leituras;
* Quantidade de leituras estáveis;
* Quantidade de leituras em atenção;
* Quantidade de leituras críticas;
* Ciclo mais crítico;
* Maior pontuação de risco;
* Conclusão geral da missão.

Essa função melhora a interpretação dos dados e transforma as leituras em informação útil para tomada de decisão.

---

## Uso de condicionais

As estruturas condicionais `if`, `elif` e `else` são utilizadas para:

* Verificar a opção escolhida no menu;
* Validar a comunicação;
* Identificar situações críticas;
* Calcular pontuação de risco;
* Classificar o status da leitura;
* Definir a conclusão do relatório.

---

## Uso de repetição

O sistema utiliza repetição em dois pontos principais:

1. `while True`: mantém o menu ativo até o usuário escolher encerrar;
2. `for`: percorre a lista de leituras para visualizar dados, executar análises, exibir alertas e gerar relatório.

Exemplo:

```python
for leitura in leituras:
    alertas = analisar_leitura(leitura)
```

---

## Relação com a Orbital AgroVision

Esta entrega mantém a narrativa geral do projeto **Orbital AgroVision — Mission TerraGuard**.

Enquanto outras disciplinas trabalham com análise em Python, IA, sensores, energia e estatística, esta parte foca no uso de estruturas de dados e algoritmos para organizar leituras, processar condições e emitir alertas básicos da missão.

O sistema representa uma versão simplificada do monitoramento operacional da missão, usando temperatura, energia e comunicação como variáveis principais.

---

## Relação com os critérios da disciplina

| Critério                   | Como foi atendido                                                          |
| -------------------------- | -------------------------------------------------------------------------- |
| Funcionamento do sistema   | O programa possui menu interativo e executa as funcionalidades principais  |
| Uso de estruturas de dados | Utiliza lista de leituras e dicionários para armazenar dados               |
| Organização do código      | O sistema foi dividido em várias funções com responsabilidades específicas |
| Lógica implementada        | Usa regras condicionais para gerar alertas, pontuação e status             |
| Demonstração prática       | O funcionamento foi registrado em prints no arquivo `demonstracao.md`      |

---

## Conclusão

O sistema atende aos requisitos da atividade ao implementar um monitoramento simples de missão espacial com menu interativo, cadastro manual, simulação automática, visualização de leituras, análise de riscos, histórico de alertas e relatório resumido.

A solução utiliza listas, dicionários, funções, condicionais e estruturas de repetição, demonstrando a aplicação prática dos conceitos de Data Structures and Algorithms no contexto da Orbital AgroVision.

