# Probabilidade em espaços discretos - Parte 5 - Probabilidade e Estatística | Aula 7

![Probabilidade em espaços discretos - Parte 5 - Probabilidade e Estatística | Aula 7](https://img.youtube.com/vi/OKjhP3cxOhk/0.jpg)](https://www.youtube.com/watch?v=OKjhP3cxOhk)

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

>$A$ = Sair um número par de caras
>$B$ = Saírem exatamente 3 caras
>$C$ = Saírem pelo menos 2 caras consecutivas

E o seguinte espaço amostral $S$

| 0 Caras | 1 Cara | 2 Caras | 3 caras | 4 Caras |
| :-----: | :----: | :-----: | :-----: | :-----: |
|  KKKK   |  CKKK  |  CCKK   |  CCCK   |  CCCC   |
|         |  KCKK  |  CKCK   |  CCKC   |         |
|         |  KKCK  |  CKKC   |  CKCC   |         |
|         |  KKKC  |  KCKC   |  KCCC   |         |
|         |        |  KKCC   |         |         |
|         |        |  KCCK   |         |         |

>$S = 16$

### 1. Sair um número par de caras

| 0 Caras  | 1 Cara | 2 Caras  | 3 caras | 4 Caras  |
| :------: | :----: | :------: | :-----: | :------: |
| **KKKK** |  CKKK  | **CCKK** |  CCCK   | **CCCC** |
|          |  KCKK  | **CKCK** |  CCKC   |          |
|          |  KKCK  | **CKKC** |  CKCC   |          |
|          |  KKKC  | **KCKC** |  KCCC   |          |
|          |        | **KKCC** |         |          |
|          |        | **KCCK** |         |          |

>$m = 8$ resultados favoráveis ao evento A (em negrito)
>
>$n = 16$ resultados possíveis
>
>$P(A) = \frac{m}{n} = \frac{8}{16} = \frac{1}{2} = 50\%$

### 2. Saírem exatamente 3 caras

| 0 Caras | 1 Cara | 2 Caras | 3 caras  | 4 Caras |
| :-----: | :----: | :-----: | :------: | :-----: |
|  KKKK   |  CKKK  |  CCKK   | **CCCK** |  CCCC   |
|         |  KCKK  |  CKCK   | **CCKC** |         |
|         |  KKCK  |  CKKC   | **CKCC** |         |
|         |  KKKC  |  KCKC   | **KCCC** |         |
|         |        |  KKCC   |          |         |
|         |        |  KCCK   |          |         |

>$m = 4$ resultados favoráveis ao evento B (em negrito)
>
>$n = 16$ resultados possíveis
>
>$P(B) = \frac{m}{n} = \frac{4}{16} = \frac{1}{4} = 25\%$

### 3. Saírem exatamente 3 caras ou um número par de caras

| 0 Caras | 1 Cara | 2 Caras  | 3 caras  | 4 Caras |
| :-----: | :----: | :------: | :------: | :-----: |
| *KKKK*  |  CKKK  |  *CCKK*  | **CCCK** | *CCCC*  |
|         |  KCKK  |  *CKCK*  | **CCKC** |         |
|         |  KKCK  |  *CKKC*  | **CKCC** |         |
|         |  KKKC  |  *KCKC*  | **KCCC** |         |
|         |        | **KKCC** |          |         |
|         |        |  *KCCK*  |          |         |

>$m = 4 + 8 = 12$
>
>* 4 resultados favoráveis ao evento B (em negrito)
>* 8 resultados favoráveis ao evento A (em itálico)
>
>$n = 16$ resultados possíveis
>
>$P(A \cup B) = \frac{m}{n} = \frac{12}{16} = \frac{3}{4} = 75\%$

### 4. Saírem exatamente 3 caras e haver pelo menos 2 caras consecutivas

| 0 Caras | 1 Cara | 2 Caras |  3 caras   | 4 Caras |
| :-----: | :----: | :-----: | :--------: | :-----: |
|  KKKK   |  CKKK  | *CCKK*  | ***CCCK*** | *CCCC*  |
|         |  KCKK  |  CKCK   | ***CCKC*** |         |
|         |  KKCK  |  CKKC   | ***CKCC*** |         |
|         |  KKKC  |  KCKC   | ***KCCC*** |         |
|         |        | *KKCC*  |            |         |
|         |        | *KCCK*  |            |         |

>$m = 4$
>
>* 4 resultados favoráveis ao evento B (em negrito)
>* 8 resultados favoráveis ao evento C (em itálico), mas apenas 4 desses também são favoráveis ao evento B
>* Portanto, 4 eventos favoráveis aos eventos B e C
>
>$n = 16$ resultados possíveis
>
>$P(B \cap C) = \frac{m}{n} = \frac{4}{16} = \frac{1}{4} = 25\%$

### 5. Saírem pelo menos 2 caras consecutivas

| 0 Caras | 1 Cara | 2 Caras  | 3 caras  | 4 Caras  |
| :-----: | :----: | :------: | :------: | :------: |
|  KKKK   |  CKKK  | **CCKK** | **CCCK** | **CCCC** |
|         |  KCKK  |   CKCK   | **CCKC** |          |
|         |  KKCK  |   CKKC   | **CKCC** |          |
|         |  KKKC  |   KCKC   | **KCCC** |          |
|         |        | **KKCC** |          |          |
|         |        | **KCCK** |          |          |

>$m = 8 resultados favoráveis ao evento C (em negrito)$
>
>$n = 16$ resultados possíveis
>
>$P(C) = \frac{m}{n} = \frac{8}{16} = \frac{1}{2} = 50\%$

### 6. Não ocorrer o evento "número par de caras e pelo menos 2 caras consecutivas

| 0 Caras | 1 Cara |  2 Caras   | 3 caras  |  4 Caras   |
| :-----: | :----: | :--------: | :------: | :--------: |
| *KKKK*  |  CKKK  | ***CCKK*** | **CCCK** | ***CCCC*** |
|         |  KCKK  |   *CKCK*   | **CCKC** |            |
|         |  KKCK  |   *CKKC*   | **CKCC** |            |
|         |  KKKC  |   *KCKC*   | **KCCC** |            |
|         |        | ***KKCC*** |          |            |
|         |        | ***KCCK*** |          |            |

>$P(A) = 8$ resultados favoráveis ao evento A (em itálico)
>
>$P(C) = 8$ resultados favoráveis ao evento C (em negrito)
>
>$n = 16$ resultados possíveis

| 0 Caras | 1 Cara |  2 Caras   | 3 caras |  4 Caras   |
| :-----: | :----: | :--------: | :-----: | :--------: |
|  KKKK   |  CKKK  | ***CCKK*** |  CCCK   | ***CCCC*** |
|         |  KCKK  |    CKCK    |  CCKC   |            |
|         |  KKCK  |    CKKC    |  CKCC   |            |
|         |  KKKC  |    KCKC    |  KCCC   |            |
|         |        | ***KKCC*** |         |            |
|         |        | ***KCCK*** |         |            |

>$P(A \cap C) = 4$ resultados favoráveis ao evento A intersecção C (em >negrito e itálico)$
>
>$P(C) = 12$ resultados não favoráveis ao evento A intersecção C (sem >destaque)
>
>$P(\overline{A \cap C}) = \frac{m}{n} = \frac{12}{16} = \frac{3}{4} = 75\%$

---
[$\blacktriangleleft$ Aula Anterior](aula-06.md) | [Início](README.md) | [Próxima Aula $\blacktriangleright$](aula-08.md)
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTUwMzU4MDkxXX0=
-->