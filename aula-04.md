# Probabilidade em espaços discretos - Parte 2 - Probabilidade e Estatística | Aula 4

[![Probabilidade em espaços discretos - Parte 2 - Probabilidade e Estatística | Aula 4](https://img.youtube.com/vi/9jAxVU8VcoQ/0.jpg)](https://www.youtube.com/watch?v=9jAxVU8VcoQ)

## Probabilidade

O que é probabilidade? 

1. Medida da ocorrência de um evento?
2. Medida baseada em registros de experiências passadas sobre a ocorrência de um evento?
3. Medida da informação sobre a ocorrência de um evento?

### Definições

#### Definição Clássica

> $p=\frac{m}{n}$

**Onde:**
> p = probabilidade
>
> m = número de resultados favoráveis
>
> n = número de resultados possíveis

Desde que todos os casos possíveis sejam igualmente favoráveis.

**Exemplo:**

Em uma cartela de rifa existem de 100 nomes. Armengado compra 5 desses nomes. A probabilidade de armengado ganhar o prêmio é calculada em:

> $p=\frac{5}{100}=5\%$

Ou seja: 5 casos favoráveis em 100 casos possíveis.

#### Definição Frequência Lista

A definição Frequência Lista define a probabilidade usando o histórico do que já aconteceu. 

> Probabilidade = limite da frequência relativa
>
> $\lim_{n \to \infty} \frac{m}{n}$

**Onde:**

> m = número de vezes que o evento ocorreu
>
>n = número de experimentos

Essa definição vale quando o número de experimentos tende ao infinito.

#### Definição Axiomática

A probabilidade é um número, associado a um evento, e que obedece 3 leis:

##### 1ª Lei:

A proabilidade de um evento é sempre maior ou igual a zero.

> $p(f) \ge 0$

##### 2ª Lei:

A probabilidade do evento certo é igual a um.

> $P(S) = 1$

##### 3ª Lei:

Probabilidade de $E \cup F$ é igual às somas das probabilidades de $E$ e $F$ no caso específico dos eventos $E$ e $F$ serem mutualmente exclusivos.

> $P(E \cup F) = P(E) + P(F)$

#### Definição subjetiva

A definição de probabilidade depende, muitas vezes, da avaliação pessoal de cada um, sendo baseada em estimativas, conceitos prévios e informações que cada um possui.

#### Resumo

Definição clássica é pouco utilizada em engenharia, pois raramente os casos possíveis são equiprováveis. Na maioria das vezes, nós temos um espaço amostral onde cada um dos eventos têm uma probabilidade diferente de ocorrer.

A definição frequencialista exige um número muito grande de experiências. Só é aplicável quando o número de eventos tende ao infinito.

A definição axiomática não permite calcular diretamente a probabilidade, mas nos oferece recursos possibilita o desenvolvimento de uma teoria, que possibilita o calculo da probabilidade de eventos complexos, tendo como base a probabilidade de eventos complementares.

#### Conclusão

Para calcular a probabilidade de um evento complexo, nós calculamos a probabilidade dos eventos elementares que formam esse evento complexo. Pra isso, pra cada evento, usamos as definições aplicáveis:

* a clássica, se os casos possíveis são equiprováveis
* a frequencialista, se tivermos um histórico
* a subjetiva, de acordo com o nível de informações

## O que é probabilidade?

> Medida da informação ou crença sobre a ocorrência de um evento

---
[&#9668; Aula Anterior](aula-03.md) | [Início](README.md) | [Próxima Aula&#9658;](aula-05.md)