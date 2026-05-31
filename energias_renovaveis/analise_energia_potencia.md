# Análise de Energia e Potência — Orbital AgroVision

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este documento apresenta a análise energética utilizada no sistema de monitoramento da missão **Mission TerraGuard**, desenvolvido para a disciplina de **Soluções em Energias Renováveis e Sustentáveis**.

A proposta é simular o acompanhamento de um módulo espacial experimental aplicado ao monitoramento agrícola, analisando bateria, luminosidade, geração solar simulada, consumo energético e saldo de energia.

---

## Objetivo da análise

O objetivo da análise é interpretar dados simulados de energia da missão para identificar situações de risco e apoiar decisões sustentáveis.

O sistema busca responder perguntas como:

* A bateria do módulo está em nível seguro?
* A luminosidade disponível permite boa geração solar?
* O consumo estimado está maior que a geração?
* É necessário ativar modo de economia de energia?
* O módulo deve priorizar funções críticas?

---

## Conceitos utilizados

## Energia

Energia representa a capacidade de realizar trabalho ou manter um sistema em funcionamento.

No projeto, a energia aparece principalmente na variável `bateria`, que indica o percentual de energia disponível no módulo de monitoramento.

Exemplo:

```text
bateria = 88%
```

Esse valor indica que o módulo possui boa disponibilidade energética.

Quando a bateria fica muito baixa, o sistema interpreta que existe risco operacional.

---

## Potência

Potência representa a taxa de uso ou geração de energia ao longo do tempo.

No sistema, a potência é usada de duas formas:

* Potência solar simulada;
* Consumo energético estimado.

A potência solar simulada representa a energia que poderia ser gerada a partir da luminosidade captada pelo módulo.

O consumo estimado representa a demanda energética necessária para manter os sensores, comunicação e processamento funcionando.

---

## Luminosidade como geração solar simulada

A variável `luminosidade` representa o potencial de captação de luz pelo módulo.

No sistema, ela é usada para simular a geração de energia por painéis solares.

A regra usada foi:

```text
potência solar simulada = luminosidade × 5
```

Exemplo:

```text
luminosidade = 75
potência solar simulada = 75 × 5 = 375 W
```

Essa regra é simplificada, mas ajuda a representar a relação entre maior luminosidade e maior geração solar.

---

## Consumo energético estimado

O consumo energético estimado parte de um valor base e aumenta quando a missão apresenta condições mais críticas.

No sistema, o consumo base é:

```text
consumo base = 280 W
```

Esse valor pode aumentar de acordo com as condições do ciclo.

Regras utilizadas:

| Condição             | Aumento no consumo |
| -------------------- | -----------------: |
| Temperatura > 35     |              +40 W |
| Comunicação < 60     |              +25 W |
| Risco ambiental > 70 |              +35 W |

Esses acréscimos representam situações em que o módulo pode precisar gastar mais energia com resfriamento, comunicação, processamento ou sensores ambientais.

---

## Saldo energético

O saldo energético é calculado pela diferença entre a geração solar simulada e o consumo estimado.

```text
saldo energético = potência solar simulada - consumo estimado
```

Se o saldo for positivo, a geração simulada é maior que o consumo.

Se o saldo for negativo, o consumo é maior que a geração, indicando risco de déficit energético.

Exemplo:

```text
potência solar simulada = 150 W
consumo estimado = 380 W

saldo energético = 150 - 380 = -230 W
```

Nesse caso, o sistema identifica que o módulo está consumindo mais energia do que consegue gerar.

---

## Regras de alerta energético

O sistema gera alertas automáticos com base nas condições energéticas da missão.

| Condição             | Alerta                                                 |
| -------------------- | ------------------------------------------------------ |
| Bateria < 50         | Atenção: bateria abaixo do nível ideal                 |
| Bateria < 20         | Bateria crítica: ativar modo de economia de energia    |
| Luminosidade < 40    | Baixa luminosidade: geração solar reduzida             |
| Saldo energético < 0 | Consumo maior que geração: risco de déficit energético |
| Risco ambiental > 70 | Risco ambiental alto: priorizar funções críticas       |

Essas regras permitem que o sistema identifique rapidamente situações críticas e recomende ações preventivas.

---

## Status energético

O sistema classifica cada ciclo da missão como:

| Status  | Significado                                                      |
| ------- | ---------------------------------------------------------------- |
| ESTÁVEL | O ciclo não apresenta risco energético relevante                 |
| ATENÇÃO | O ciclo apresenta sinais de risco e exige acompanhamento         |
| CRÍTICO | O ciclo apresenta risco energético elevado e exige ação imediata |

A classificação é definida por uma pontuação baseada em bateria, luminosidade, saldo energético e risco ambiental.

---

## Decisões automáticas

Além de gerar alertas, o sistema também apresenta uma decisão automática para cada ciclo.

Exemplos de decisões:

| Situação             | Decisão automática                                           |
| -------------------- | ------------------------------------------------------------ |
| Bateria < 20         | Ativar economia de energia e desligar funções não essenciais |
| Saldo energético < 0 | Reduzir consumo e priorizar comunicação com a base           |
| Luminosidade < 40    | Aguardar maior geração solar ou reduzir processamento        |
| Risco ambiental > 70 | Manter monitoramento ativo e priorizar sensores ambientais   |
| Sem risco relevante  | Manter operação energética normal                            |

Essas decisões representam uma tomada de decisão básica diante de situações críticas simuladas.

---

## Modo de economia de energia

O sistema também simula um modo de economia de energia.

Quando um ciclo está em estado crítico, o consumo estimado é reduzido em 20%.

A regra usada foi:

```text
consumo com economia = consumo original × 0,8
```

Exemplo:

```text
consumo original = 380 W
consumo com economia = 380 × 0,8 = 304 W
economia estimada = 76 W
```

Esse recurso representa uma estratégia de preservação energética em cenários críticos.

---

## Relação com energias renováveis

A energia solar simulada representa o uso de uma fonte renovável para manter o funcionamento do módulo espacial.

No contexto da Orbital AgroVision, essa lógica é importante porque sensores remotos e módulos de monitoramento agrícola podem operar em áreas distantes, onde o uso eficiente de energia é essencial.

A luminosidade funciona como uma variável simplificada para estimar a disponibilidade de geração solar.

Quanto maior a luminosidade, maior o potencial de geração energética do sistema.

---

## Relação com sustentabilidade

O monitoramento energético contribui para a sustentabilidade porque ajuda a:

* Reduzir desperdício de energia;
* Priorizar funções críticas;
* Evitar falhas por baixa bateria;
* Usar geração solar simulada como fonte renovável;
* Apoiar decisões inteligentes no agronegócio;
* Manter sensores ambientais ativos em áreas agrícolas de risco.

Assim, o sistema conecta tecnologia espacial, energia renovável e tomada de decisão sustentável.

---

## Relação com a Orbital AgroVision

A Orbital AgroVision simula o uso de tecnologias espaciais para apoiar o agronegócio sustentável.

Nesta disciplina, o foco está no aspecto energético da missão.

A **Mission TerraGuard** precisa manter seus módulos funcionando para continuar monitorando áreas agrícolas. Por isso, o sistema energético deve acompanhar bateria, geração solar, consumo e risco ambiental.

Quando há baixa energia, baixa luminosidade ou consumo elevado, o sistema recomenda ações para preservar recursos e manter a operação segura.

---

## Conclusão

A análise de energia e potência mostra como dados simulados podem ser usados para avaliar a condição energética de uma missão espacial experimental.

O sistema calcula geração solar simulada, consumo estimado, saldo energético, status do ciclo, alertas e decisões automáticas.

Dessa forma, a entrega atende à proposta da disciplina ao aplicar conceitos de energia, potência, energias renováveis e sustentabilidade em uma solução computacional ligada à Orbital AgroVision.

