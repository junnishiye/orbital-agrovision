# Demonstração Prática — Data Structures and Algorithms

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este arquivo apresenta as evidências de execução do sistema de monitoramento desenvolvido para a disciplina de **Data Structures and Algorithms**.

A demonstração mostra o funcionamento do menu interativo, cadastro de leituras, visualização dos dados, análise automática e histórico de alertas.

---

## 1. Menu principal

O sistema inicia exibindo um menu com as opções disponíveis para o usuário.

![Menu principal](../assets/prints/data_menu.png)

---

## 2. Inserção de nova leitura

Nesta etapa, o usuário insere uma nova leitura da missão, informando temperatura, nível de energia e status da comunicação.

![Inserção de nova leitura](../assets/prints/data_inserir_leitura.png)

---

## 3. Visualização das leituras cadastradas

O sistema exibe todas as leituras armazenadas na lista `leituras`, incluindo temperatura, energia, comunicação e status operacional.

![Visualização das leituras](../assets/prints/data_visualizar_leituras.png)

---

## 4. Análise automática das leituras

O sistema percorre as leituras cadastradas e aplica as regras de verificação automática:

- Temperatura > 80 → alerta de superaquecimento;
- Energia < 20 → economia de energia;
- Comunicação = 0 → falha de comunicação.

![Análise automática](../assets/prints/data_analise.png)

---

## 5. Histórico de alertas

O histórico apresenta as leituras que geraram alertas durante a execução do sistema.

![Histórico de alertas](../assets/prints/data_historico.png)

---

## Conclusão da demonstração

A demonstração comprova que o sistema executa corretamente as principais funcionalidades exigidas:

- Menu interativo;
- Cadastro de dados;
- Visualização das leituras;
- Análise automática;
- Histórico de alertas;
- Uso de listas, funções, condicionais e repetição.
