# Roteiro de Apresentação(BASE) – Orbital AgroVision | Mission TerraGuard

# Introdução

Olá,

Apresentamos o projeto Orbital AgroVision – Mission TerraGuard, desenvolvido para a Global Solution 2026.1.

Nosso projeto propõe uma solução inspirada em tecnologias espaciais para o monitoramento inteligente de áreas agrícolas, utilizando sensores, sistemas embarcados e automação para identificar riscos ambientais e operacionais.

---

# Problema

No agronegócio, decisões precisam ser tomadas rapidamente para evitar perdas causadas por condições ambientais adversas.

Temperaturas elevadas, baixa luminosidade, falhas operacionais e instabilidades podem impactar diretamente a produtividade e a sustentabilidade das áreas agrícolas.

Por isso, desenvolvemos um sistema capaz de monitorar essas condições em tempo real e alertar o operador sempre que uma situação de risco for identificada.

---

# Solução Proposta

A solução consiste em um sistema baseado em Arduino, responsável por coletar dados de diferentes sensores e apresentar as informações em um painel LCD.

O sistema monitora:

* Temperatura, através do sensor TMP36;
* Luminosidade, através do sensor LDR;
* Vibração, simulada por um potenciômetro.

Esses dados são processados continuamente e classificados em três níveis:

* STATUS OK;
* ATENÇÃO;
* RISCO ALTO.

---

# Demonstração

Neste momento podemos observar o circuito completo desenvolvido no Tinkercad.

O LCD exibe os dados de temperatura, luminosidade e vibração em tempo real.

Quando os parâmetros permanecem dentro dos limites aceitáveis, o sistema apresenta o status "STATUS OK" e aciona o LED verde.

Ao identificar condições que merecem atenção, o sistema exibe "ATENÇÃO" e aciona o LED amarelo.

Quando uma situação crítica é detectada, como temperatura excessiva ou vibração elevada, o sistema apresenta "RISCO ALTO", aciona o LED vermelho e ativa o buzzer sonoro para alertar o operador.

---

# Aplicação no Agronegócio

O Orbital AgroVision demonstra como tecnologias inspiradas em missões espaciais podem ser aplicadas ao monitoramento agrícola.

A solução permite acompanhar condições ambientais, antecipar riscos e apoiar decisões mais rápidas e sustentáveis, contribuindo para a eficiência operacional e a preservação dos recursos naturais.

---

# Conclusão

Concluímos que o projeto atingiu seus objetivos ao integrar sensores, programação, eletrônica e automação em uma solução funcional de monitoramento inteligente.

O sistema realiza leituras em tempo real, classifica riscos automaticamente e fornece alertas visuais e sonoros para auxiliar a tomada de decisão.

Obrigado pela atenção.
