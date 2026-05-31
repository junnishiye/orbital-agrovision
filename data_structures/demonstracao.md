# Demonstração Prática — Data Structures and Algorithms

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este arquivo apresenta as evidências de execução do sistema de monitoramento desenvolvido para a disciplina de **Data Structures and Algorithms**.

A demonstração mostra o funcionamento do menu interativo, cadastro de leituras, simulação automática, visualização dos dados, análise automática, histórico de alertas e relatório resumido.

---

## 1. Menu principal

O sistema inicia exibindo um menu com as opções disponíveis para o usuário.

![Menu principal](../assets/prints/data_menu.png)

---

## 2. Simulação automática de leitura

Nesta etapa, o sistema gera automaticamente uma nova leitura simulada da missão.

![Simulação automática](../assets/prints/data_simulacao.png)

---

## 3. Inserção manual de nova leitura

Nesta etapa, o usuário insere manualmente uma nova leitura da missão, informando temperatura, nível de energia e status da comunicação.

![Inserção manual de leitura](../assets/prints/data_inserir_leitura.png)

---

## 4. Visualização das leituras cadastradas

O sistema exibe todas as leituras armazenadas na lista `leituras`, incluindo ciclo, temperatura, energia, comunicação, pontuação de risco e status operacional.

![Visualização das leituras](../assets/prints/data_visualizar_leituras.png)

---

## 5. Análise automática das leituras

O sistema percorre as leituras cadastradas e aplica as regras de verificação automática:

- Temperatura > 80 → alerta de superaquecimento;
- Energia < 20 → economia de energia;
- Comunicação = 0 → falha de comunicação.

![Análise automática](../assets/prints/data_analise.png)

---

## 6. Histórico de alertas

O sistema apresenta apenas os ciclos que registraram alertas reais, facilitando a identificação de situações críticas.

![Histórico de alertas](../assets/prints/data_alertas.png)

---

## 7. Relatório resumido

O sistema gera um resumo geral da missão, mostrando total de leituras, quantidade de estados estáveis, em atenção e críticos, além do ciclo mais crítico.

![Relatório resumido](../assets/prints/data_relatorio.png)

---

## Conclusão da demonstração

A demonstração comprova que o sistema executa corretamente as principais funcionalidades exigidas:

- Menu interativo;
- Inserção manual de dados;
- Simulação automática de leituras;
- Visualização das leituras;
- Análise automática;
- Histórico de alertas;
- Relatório resumido;
- Uso de listas, funções, condicionais e repetição.
