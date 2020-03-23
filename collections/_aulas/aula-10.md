---
title: Aula 10
description: Teoremas de probabilidade - Parte 3 - Probabilidade e Estatística | Aula 10
video: NYfDVDvYuwQ
name: aula-10.md
anterior: aula-09.md
proximo: aula-11.md
permalink: aulas/aula-10/
---

## Resolução do exercício da [Aula 09]({{site.baseurl}}{{ page.previous.url }})

No caso da megasena, o espaço amostral é composto por 60 números, de 01 a 60, e a pessoa precisa acertar os 6 números que foram sorteados.

### 1. A chance de sair o número 6 já na primeira bola do sorteio

Nesse caso, só existe um sucesso, ou seja, sair 6 na primeira possibilidade. Portanto:

> $$P(A) = \frac{1}{60}$$

### 2. A chance de sair o número 6 na primeira bola e o 16 na segunda

No primeiro caso, temos 1 chance em 60 de sair a bola 6. Mas, no segundo caso, teos 1 chance em 59, pois já saiu uma bola (6) e o espaço amostral diminuiu.

Portanto:

> $$P(A \cap B) = \frac{1}{60} . \frac{1}{59} = \frac{1}{3540}$$

### 3. A chance de acertar os 6 números

Para responder essa pergunta, precisamos da fórmula da combinação sem repetição.

> $${C^{n}_{s}} = {n \choose s} = \frac{n!}{s! \cdot (n - s)!}$$
>
> $${C_{60,6}} = \frac{60!}{6! \cdot (60 - 6)! } = \frac{60!}{6! \cdot 54!} = \frac{60 \cdot 59 \cdot 58 \cdot 57 \cdot 56 \cdot 55 \cdot \sout  54!}{6! \cdot \sout 54!}$$
>
> $${C_{60,6}} \frac{60 \cdot 59 \cdot 58 \cdot 57 \cdot 56 \cdot 55}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 50.063.860$$
>
> $$P(C) = \frac{1}{50.063.860}$$

### 4. A chance de acertar a quina

> $$ P(D) = \frac {C_{6,5} \dot C_{54,1}}{C_{60,6}} = \frac{\binom{6}{5} \dot \binom{54}{1}}{\binom{60}{6}} $$
>
> $$ C_{6,5} = \binom{6}{5} = \frac{6!}{5! \dot (6 - 5)!}$$
> 
> $$ C_{54,1} = \binom{54}{1} = \frac{54!}{1! \dot (54 - 1)!}$$
> 
> $$ C_{60,1} = \binom{60}{6} = \frac{60!}{60! \dot (60 - 6)!}$$

