---
title: Probabilidade em espaços discretos - Parte 2 - Probabilidade e Estatística | Aula 4
video: 9jAxVU8VcoQ
previous: aula-03.md
next: aula-05.md
---
# Teoremas de probabilidade - Parte 3 - Probabilidade e Estatística | Aula 10


[![Teoremas de probabilidade - Parte 3 - Probabilidade e Estatística | Aula 10](https://img.youtube.com/vi/NYfDVDvYuwQ/0.jpg)](https://www.youtube.com/watch?v=NYfDVDvYuwQ)

## Resolução do exercício da [Aula 09](aula-09.md)

No caso da megasena, o espaço amostral é composto por 60 números, de 01 a 60.

## 1. A chance de sair o número 6 já na primeira bola do sorteio

> $P(A) = \frac{1}{60}$

## 2. A chance de sair o número 6 na primeira bola e o 16 na segunda

No primeiro caso, temos 1 chance em 60 de sair a bola 6. Mas, no segundo caso, teos 1 chance em 59, pois já saiu uma bola (6) e o espaço amostral diminuiu.

Portanto:

> $P(A \cap B) = \frac{1}{60} . \frac{1}{59} = \frac{1}{3540}$

## 3. A chance de acertar os 6 números

Para responder essa pergunta, precisamos da fórmula da combinação sem repetição.

> ${C^{n}_{s}} = {n \choose s} = \frac{n!}{s! \cdot (n - s)!}$
>
> ${C_{60,6}} = \frac{60!}{6! \cdot (60 - 6)! } = \frac{60!}{6! \cdot 54!} = \frac{60 \cdot 59 \cdot 58 \cdot 57 \cdot 56 \cdot 55 \cdot \sout  54!}{6! \cdot \sout 54!}$
>
> ${C_{60,6}} \frac{60 \cdot 59 \cdot 58 \cdot 57 \cdot 56 \cdot 55}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 50.063.860$
>
> $P(C) = \frac{1}{50.063.860}$
## 4. A chance de aertar a quina

---
[&#9668; Aula Anterior](aula-09.md) | [Início](README.md) | [Próxima Aula &#9658;](aula-11.md)