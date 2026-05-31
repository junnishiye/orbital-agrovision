# Sustentabilidade — Orbital AgroVision

## Projeto

**Orbital AgroVision — Mission TerraGuard**

Este documento explica como o sistema de monitoramento energético da **Mission TerraGuard** se relaciona com sustentabilidade, eficiência energética e apoio ao agronegócio sustentável.

---

## Relação entre energia e sustentabilidade

Em sistemas de monitoramento remoto, a energia é um recurso essencial.

Se um módulo de monitoramento fica sem bateria, ele pode deixar de coletar dados importantes sobre temperatura, comunicação, risco ambiental e condições operacionais.

Por isso, controlar o consumo energético é uma forma de aumentar a eficiência da operação e reduzir desperdícios.

No projeto, o sistema analisa:

* Nível de bateria;
* Luminosidade;
* Potência solar simulada;
* Consumo estimado;
* Saldo energético;
* Risco ambiental;
* Necessidade de economia de energia.

---

## Uso de energia renovável simulada

A variável `luminosidade` representa o potencial de geração solar do módulo.

Quanto maior a luminosidade, maior a potência solar simulada.

A regra usada no sistema é:

```text
potência solar simulada = luminosidade × 5
```

Essa simulação representa o uso de energia solar como fonte renovável para alimentar sensores e módulos de monitoramento.

---

## Economia de energia

Quando o sistema identifica baixa bateria ou consumo maior que a geração solar simulada, ele recomenda ações de economia.

Exemplos:

* Ativar modo de economia de energia;
* Reduzir consumo;
* Desligar funções não essenciais;
* Priorizar comunicação com a base;
* Priorizar sensores ambientais.

Essas ações ajudam a manter a missão funcionando mesmo em situações críticas.

---

## Sustentabilidade no agronegócio

A Orbital AgroVision simula o monitoramento de áreas agrícolas por tecnologias espaciais.

Esse monitoramento pode apoiar decisões sustentáveis no agronegócio, como:

* Identificar áreas com risco ambiental;
* Reduzir desperdício de recursos;
* Acompanhar condições críticas de temperatura;
* Manter sensores ativos em áreas remotas;
* Apoiar decisões rápidas em situações de risco;
* Usar energia de forma mais eficiente.

A proposta ajuda produtores e gestores ambientais a tomar decisões com base em dados, reduzindo impactos e melhorando a eficiência da produção.

---

## Redução de desperdícios

O sistema contribui para a redução de desperdícios porque identifica quando a energia está sendo usada de forma crítica.

Quando o saldo energético fica negativo, significa que o consumo estimado é maior que a geração solar simulada.

Nesse caso, o sistema recomenda reduzir consumo e priorizar funções importantes.

Isso evita que o módulo gaste energia em funções menos importantes durante momentos de risco.

---

## Priorização de funções críticas

Em cenários críticos, nem todos os recursos do módulo devem ter a mesma prioridade.

O sistema pode recomendar que a missão priorize:

* Comunicação com a base;
* Sensores ambientais;
* Monitoramento de risco;
* Preservação da bateria;
* Operações essenciais.

Essa lógica representa uma tomada de decisão básica voltada à segurança e à sustentabilidade operacional.

---

## Impacto da solução

A solução proposta mostra como tecnologia, energia renovável e sustentabilidade podem ser integradas.

O sistema não apenas exibe dados, mas também interpreta a situação energética e recomenda ações.

Isso torna a Orbital AgroVision mais próxima de uma solução inteligente, capaz de apoiar decisões em ambientes agrícolas monitorados por tecnologia espacial.

---

## Conclusão

A análise energética da Mission TerraGuard mostra que sustentabilidade não depende apenas de usar fontes renováveis, mas também de usar energia de forma inteligente.

Ao monitorar bateria, luminosidade, consumo e risco ambiental, o sistema ajuda a preservar recursos, evitar desperdícios e manter o monitoramento agrícola ativo.

Dessa forma, a Orbital AgroVision conecta energia renovável, eficiência operacional e sustentabilidade aplicada ao agronegócio.

