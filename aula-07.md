# Probabilidade em espaços discretos - Parte 5 - Probabilidade e Estatística | Aula 7

[![Probabilidade em espaços discretos - Parte 5 - Probabilidade e Estatística | Aula 7](https://img.youtube.com/vi/OKjhP3cxOhk/0.jpg)](https://www.youtube.com/watch?v=OKjhP3cxOhk)

## Lançamentos de moedas

Serão lançadas 4 moedas, honestas, sucessivamente. Calcule as seguintes probabilidades.

1. Sair um número par de caras
2. Saírem exatamente 3 caras
3. Saírem exatamente 3 caras ou um número par de caras
4. Saírem exatamente 3 caras e haver pelo menos 2 caras consecutivas
5. Saírem pelo menos 2 caras consecutivas
6. Não ocorrer o evento "número par de caras e pelo menos 2 caras consecutivas

## Resolução

Temos, inicialmente, os seguintes eventos elementares:

$A$ = Sair um número par de caras
$B$ = Saírem exatamente 3 caras
$C$ = Saírem pelo menos 2 caras consecutivas

E o seguinte espaço amostral $S$

| 0 Caras | 1 Cara | 2 Caras | 3 caras | 4 Caras |
| :-----: | :----: | :-----: | :-----: | :-----: |
|  KKKK   |  CKKK  |  CCKK   |  CCCK   |  CCCC   |
|         |  KCKK  |  CKCK   |  CCKC   |         |
|         |  KKCK  |  CKKC   |  CKCC   |         |
|         |  KKKC  |  KCKC   |  KCCC   |         |
|         |        |  KKCK   |         |         |
|         |        |  KCCK   |         |         |

$S = 16$

### 1. Sair um número par de caras

| 0 Caras  | 1 Cara | 2 Caras  | 3 caras | 4 Caras  |
| :------: | :----: | :------: | :-----: | :------: |
| **KKKK** |  CKKK  | **CCKK** |  CCCK   | **CCCC** |
|          |  KCKK  | **CKCK** |  CCKC   |          |
|          |  KKCK  | **CKKC** |  CKCC   |          |
|          |  KKKC  | **KCKC** |  KCCC   |          |
|          |        | **KKCK** |         |          |
|          |        | **KCCK** |         |          |

$m = 8$ resultados favoráveis ao evento A (em negrito)
$n = 16$ ewsultados possíveis

$P(A) = \frac{m}{n} = \frac{8}{16} = \frac{1}{2} = 50\%$

### 2. Saírem exatamente 3 caras

| 0 Caras | 1 Cara | 2 Caras | 3 caras  | 4 Caras |
| :-----: | :----: | :-----: | :------: | :-----: |
|  KKKK   |  CKKK  |  CCKK   | **CCCK** |  CCCC   |
|         |  KCKK  |  CKCK   | **CCKC** |         |
|         |  KKCK  |  CKKC   | **CKCC** |         |
|         |  KKKC  |  KCKC   | **KCCC** |         |
|         |        |  KKCK   |          |         |
|         |        |  KCCK   |          |         |




---
[$\blacktriangleleft$ Aula Anterior](aula-06.md) | [Início](README.md) | [Próxima Aula $\blacktriangleright$](aula-08.md)