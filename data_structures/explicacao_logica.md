# Explicação da Lógica — Data Structures and Algorithms

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este sistema simula o monitoramento básico de uma missão espacial experimental aplicada ao contexto da Orbital AgroVision.

A proposta é acompanhar informações operacionais da missão, como temperatura, energia e comunicação, analisando automaticamente se existe alguma condição de risco.

---

## Objetivo do sistema

O objetivo do programa é permitir que o usuário monitore informações básicas da missão por meio de um menu interativo.

O sistema permite:

- Inserir novas leituras;
- Visualizar leituras cadastradas;
- Executar análise automática;
- Consultar histórico de alertas;
- Encerrar o sistema.

---

## Dados monitorados

Cada leitura da missão possui as seguintes informações:

| Dado | Descrição |
|---|---|
| `temperatura` | Temperatura registrada na missão |
| `energia` | Nível de energia disponível |
| `comunicacao` | Estado da comunicação, sendo 1 para ativa e 0 para falha |
| `status` | Resultado geral da leitura |

---

## Estrutura de dados utilizada

O sistema utiliza uma lista chamada `leituras`.

Essa lista armazena várias leituras da missão. Cada leitura é representada por um dicionário contendo temperatura, energia, comunicação e status.

Exemplo:

```python
leituras = [
    {
        "temperatura": 24,
        "energia": 88,
        "comunicacao": 1,
        "status": "Operação normal"
    }
]
