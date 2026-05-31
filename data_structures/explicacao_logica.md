# Explicação da Lógica — Data Structures and Algorithms

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este sistema simula o monitoramento operacional de uma missão espacial experimental aplicada ao contexto da Orbital AgroVision.

A proposta é acompanhar informações básicas da missão, como temperatura, energia e comunicação, utilizando estruturas de dados, funções, condicionais, repetição e uma interface gráfica para identificar situações de risco e organizar as leituras.

---

## Objetivo do sistema

O objetivo do programa é permitir que o usuário monitore dados simulados da missão por meio de uma interface gráfica.

O sistema permite:

* Inserir uma nova leitura manual;
* Simular uma leitura automática;
* Visualizar leituras cadastradas em uma tabela;
* Executar análise automática das leituras;
* Consultar histórico de alertas;
* Gerar relatório resumido da missão;
* Encerrar o sistema.

---

## Interface gráfica

O sistema foi desenvolvido com a biblioteca `tkinter`, permitindo uma interação mais clara com o usuário.

A interface possui:

* Campos para inserir temperatura, energia e comunicação;
* Botão para inserir leitura manual;
* Botão para simular leitura automática;
* Tabela com as leituras cadastradas;
* Botão para executar análise;
* Botão para visualizar histórico de alertas;
* Botão para gerar relatório resumido;
* Área de texto para exibir os resultados.

---

## Dados monitorados

Cada leitura da missão possui as seguintes informações:

| Dado          | Descrição                                                |
| ------------- | -------------------------------------------------------- |
| `ciclo`       | Identificação sequencial da leitura                      |
| `temperatura` | Temperatura registrada na missão                         |
| `energia`     | Nível de energia disponível                              |
| `comunicacao` | Estado da comunicação, sendo 1 para ativa e 0 para falha |
| `pontuacao`   | Pontuação de risco calculada                             |
| `status`      | Classificação geral da leitura                           |

---

## Estrutura de dados utilizada

O sistema utiliza uma lista chamada `leituras`.

Essa lista armazena várias leituras da missão. Cada leitura é representada por um dicionário contendo ciclo, temperatura, energia, comunicação, pontuação e status.

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

A lista funciona como histórico das leituras registradas durante a execução do programa.

O uso de dicionários facilita a organização dos dados, pois cada valor possui uma chave clara, como `temperatura`, `energia`, `comunicacao`, `pontuacao` e `status`.

---

## Funções utilizadas

O código foi dividido em funções para melhorar a organização e facilitar a manutenção.

| Função                         | Finalidade                                                 |
| ------------------------------ | ---------------------------------------------------------- |
| `calcular_pontuacao()`         | Calcula a pontuação de risco da leitura                    |
| `classificar_status()`         | Classifica a leitura como estável, atenção ou crítico      |
| `analisar_leitura()`           | Verifica as condições de risco e gera alertas              |
| `criar_leitura()`              | Cria uma nova leitura com ciclo, status e pontuação        |
| `inserir_leitura_manual()`     | Cadastra uma nova leitura a partir dos campos da interface |
| `simular_leitura_automatica()` | Gera uma leitura simulada automaticamente                  |
| `atualizar_tabela()`           | Atualiza a tabela da interface gráfica                     |
| `executar_analise()`           | Analisa todas as leituras e exibe os alertas               |
| `ver_historico_alertas()`      | Mostra apenas ciclos com alertas reais                     |
| `gerar_relatorio_resumido()`   | Gera um resumo geral da missão                             |
| `limpar_campos()`              | Limpa os campos após o cadastro                            |
| `encerrar_sistema()`           | Fecha a interface gráfica                                  |

---

## Regras de análise

O sistema utiliza as regras principais exigidas na atividade:

| Condição         | Resposta do sistema         |
| ---------------- | --------------------------- |
| Temperatura > 80 | Alerta de superaquecimento  |
| Energia < 20     | Economia de energia ativada |
| Comunicação = 0  | Falha de comunicação        |

Essas regras são aplicadas na função `analisar_leitura()`.

---

## Pontuação de risco

Cada condição crítica aumenta a pontuação de risco da leitura.

| Condição         | Pontuação |
| ---------------- | --------: |
| Temperatura > 80 | +2 pontos |
| Energia < 20     | +2 pontos |
| Comunicação = 0  | +2 pontos |

A função `calcular_pontuacao()` soma esses pontos e retorna a pontuação final da leitura.

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

Após o cálculo da pontuação, o sistema classifica a leitura:

|  Pontuação | Status  |
| ---------: | ------- |
|          0 | ESTÁVEL |
|      1 a 2 | ATENÇÃO |
| Acima de 2 | CRÍTICO |

Essa classificação ajuda a identificar rapidamente a situação da missão em cada ciclo.

---

## Inserção manual de leitura

Na inserção manual, o usuário informa:

* Temperatura;
* Energia;
* Comunicação.

Depois disso, o sistema:

1. Lê os valores digitados;
2. Calcula a pontuação de risco;
3. Classifica o status;
4. Armazena a leitura na lista `leituras`;
5. Atualiza a tabela da interface;
6. Exibe uma mensagem informando que a leitura foi cadastrada.

---

## Simulação automática de leitura

A simulação automática gera uma leitura a partir de cenários definidos no código.

Essa funcionalidade representa a entrada automática de dados por sensores simulados, mantendo a proposta de monitoramento operacional da missão.

Após gerar a leitura simulada, o sistema calcula a pontuação de risco, classifica o status e atualiza a tabela da interface gráfica.

---

## Visualização das leituras

As leituras são exibidas em uma tabela da interface gráfica.

A tabela mostra:

* Ciclo;
* Temperatura;
* Energia;
* Comunicação;
* Pontuação;
* Status.

Isso facilita a visualização dos dados cadastrados e permite acompanhar a evolução das leituras da missão.

---

## Análise automática

Ao clicar no botão de análise, o sistema percorre todas as leituras armazenadas na lista `leituras`.

Para cada leitura, ele verifica:

* Se a temperatura passou de 80;
* Se a energia está abaixo de 20;
* Se a comunicação falhou.

Os alertas encontrados são exibidos na área de saída da interface.

Exemplo:

```python
if leitura["temperatura"] > 80:
    alertas.append("Alerta de superaquecimento")
```

---

## Histórico de alertas

O histórico de alertas mostra apenas as leituras que possuem alertas reais.

Isso evita poluir a visualização com ciclos estáveis e facilita a identificação dos principais problemas da missão.

O sistema percorre todas as leituras e filtra os alertas, exibindo apenas situações como superaquecimento, economia de energia ativada ou falha de comunicação.

---

## Relatório resumido

O relatório resumido apresenta uma visão geral da missão.

Ele mostra:

* Total de leituras;
* Quantidade de leituras estáveis;
* Quantidade de leituras em atenção;
* Quantidade de leituras críticas;
* Ciclo mais crítico;
* Maior pontuação de risco;
* Conclusão geral da missão.

Essa etapa transforma os dados cadastrados em uma visão resumida da operação, ajudando a interpretar o estado geral da missão.

---

## Uso de condicionais

As estruturas condicionais `if`, `elif` e `else` são usadas para:

* Validar os valores digitados;
* Verificar situações de risco;
* Calcular a pontuação;
* Classificar o status;
* Definir a conclusão do relatório;
* Controlar respostas do sistema.

Exemplo:

```python
if temperatura > 80:
    pontuacao += 2
elif pontuacao <= 2:
    status = "ATENÇÃO"
else:
    status = "CRÍTICO"
```

---

## Uso de repetição

O sistema utiliza repetição principalmente com `for`.

A repetição é usada para percorrer a lista de leituras em diferentes momentos:

* Atualização da tabela;
* Execução da análise;
* Histórico de alertas;
* Relatório resumido.

Exemplo:

```python
for leitura in leituras:
    alertas = analisar_leitura(leitura)
```

Mesmo usando interface gráfica, o sistema continua aplicando conceitos de repetição para processar todos os dados armazenados.

---

## Uso de estruturas de dados

O sistema utiliza duas estruturas principais:

| Estrutura  | Uso no sistema                                    |
| ---------- | ------------------------------------------------- |
| Lista      | Armazena todas as leituras da missão              |
| Dicionário | Representa cada leitura individual com seus dados |

A lista `leituras` funciona como um histórico em memória. Cada novo dado inserido manualmente ou simulado automaticamente é adicionado a essa lista.

Cada dicionário representa uma leitura da missão, contendo dados como temperatura, energia, comunicação, pontuação e status.

---

## Relação com a Orbital AgroVision

Esta entrega mantém a narrativa geral do projeto **Orbital AgroVision — Mission TerraGuard**.

A Mission TerraGuard simula o monitoramento de uma operação espacial voltada ao agronegócio sustentável. Nesta disciplina, o foco está no uso de estruturas de dados e algoritmos para organizar leituras, processar condições e emitir alertas básicos da missão.

O sistema representa uma versão simplificada do monitoramento operacional da Orbital AgroVision, usando temperatura, energia e comunicação como variáveis principais.

---

## Relação com os critérios da disciplina

| Critério                   | Como foi atendido                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Funcionamento do sistema   | O programa possui interface gráfica funcional com cadastro, simulação, análise, histórico e relatório |
| Uso de estruturas de dados | Utiliza lista de leituras e dicionários para armazenar os dados                                       |
| Organização do código      | O sistema foi dividido em funções específicas e reutilizáveis                                         |
| Lógica implementada        | Usa regras condicionais para gerar alertas, pontuação e status                                        |
| Demonstração prática       | O funcionamento foi registrado em prints no arquivo `demonstracao.md`                                 |

---

## Conclusão

O sistema atende aos requisitos da atividade ao implementar um monitoramento de missão espacial com interface gráfica, cadastro manual, simulação automática, visualização em tabela, análise de riscos, histórico de alertas e relatório resumido.

A solução utiliza listas, dicionários, funções, condicionais e repetição, demonstrando a aplicação prática dos conceitos de Data Structures and Algorithms no contexto da Orbital AgroVision.

