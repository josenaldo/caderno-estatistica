---
title: Aula 004
description: Tipos de Amostragem
permalink: aulas/aula-004
videos: vcTQCIfz9_M olHF_ICKKpM xi7CNuYgZ_0 pgdh3wapzJY 36ulultiNoM HMcGa0X9nEQ Tk-7fTtUP_Y 5xWb9Nyttcc H1jq8bEvl34 PNdMANe96cU EIf8x6vucRs tNSibIaX_E4 _7LOGnu-KIY 7BDijqvFSNE SLZ_zueJonQ
---

Na classificação geral do levantamento de coleta de amostra, ou amostragem, temos duas possibilidades de amostragem:

- Não Probabilística - Cada elemento tem chances diferentes de aparecer na amostra
- Probabilística - cada elemento da população tem chances iguais de aparecer na amostra

{% include imagem.html
    url="assets/images/aula-004/tipos-de-amostragem.jpeg"
    description="Tipos de Amostragem" %}

### Amostragem Não Probabilística

Também chamada de Coleta Não Aleatória. Ao realizar esse tipo de coleta, o pesquisador escolhe, de maneira deliberada, os elementos da amostra. Para isso, ele se utiliza de seus próprios critérios.

Esse tipo de amostra é classificada em 3 tipos: intencional, voluntária e acidental.

O problema desse tipo de amostragem é que não se conhece a probabilidade de cada unidade amostral pertencer à amostra. Ou seja, não se sabe o grau de similaridade da amostra com a população. Por isso essas técnicas não garantem a ausência de vícios.

Dessas forma, não há problema em se usar esse tipo de técnica, desde que isso seja deixado claro no estudo e que os resultados limitem-se apenas ao grupo escolhido e não a toda população.

#### Amostragem Acidental

Na amostragem acidental, a seleção dos elementos da amostra acaba ocorrendo ao acaso, de forma acidental. Por exemplo, você sendo abordado por um entrevistador em um local público. O entrevistador não estava ali esperando por você. Ele estava ali, parado, em um local onde muita gente passa e, calhou de ser você uma das pessoas escolhidas, apenas porque você estava passando no momento.

#### Amostragem Intencional

É um tipo de abordagem derivada da acidental. A diferença é que existe um filtro, em que apenas pessoas de interesse serão selecionadas e/ou abordadas pelo entrevistador.

{% include imagem.html
    url="assets/images/aula-004/amostragem-intencional.svg"
    description="Amostragem Intencional" %}

#### Amostragem Proporcional ou Amostragem por Quotas

Na amostragem proporcional, a amostra é uma miniatura da população, mantendo as mesmas proporções que a população.

Nessa amostragem,a coleta começa, normalmente, de forma Acidental e, à medida que mais indivíduos vão sendo coletados, ela começa a se tornar Intencional, de forma a garantir que as proporções continuem iguais às da população.

{% include imagem.html
    url="assets/images/aula-004/amostragem-proporcional.svg"
    description="Amostragem Proporcional" %}

#### Amostragem Desproporcional

Na Amostragem Desproporcional, você vai pegar, pra cada categoria, uma quantidade diferente daquela calculada na Amostragem Proporcional.

### Amostragem Probabilística

Também chamada de Coleta Aleatória. Ao realizar esse tipo de coleta, o pesquisador escolhe um método simples, sistemático, estratificado ou por conglomerado. Ele sabe que cada unidade amostral tem uma probabilidade conhecida e diferente de zero de aparecer na amostra.

#### Amostragem Probabilística Aleatória Simples

Os elementos são escolhidos de maneira puramente aleatória. Pode se usar sorteio, um sistema informatizado ou qualquer outro meio que produza essa aleatoriedade.

{: .blockquote}
> Exemplo:
>
> E um grupo de 80 pessoas, precisamos de uma amostra de 20 pessoas. Então, faremos da seguinte forma:
>
> 1) Enumeramos 80 pessoas
>
> 2) Realizamos o sorteio de 20 números, de 1 a 80. Pode ser no formato de bingo.
>
> 3) Após o sorteio, teremos 20 pessoas selecionadas para compor a amostra, ou seja, 25% da população.

Nesse tipo de amostragem, é importante que a aleatoriedade seja mantida na hora de escolher cada elemento. Algumas ferramenta que podem ajudar nesse sorteio:

- Tabelas de números aleatórios
- Excel
- Calculadora científica
- Sites de sorteio
- Um programa simples, escrito em qualquer linguagem de programação que tenha uma biblioteca de randomização, como Python, Java, C#, etc.

#### Amostragem Probabilística Sistemática

Na Amostragem Probabilística Sistemática, os elementos da amostra são escolhidos a partir de um fator de repetição, intervalo fixo. isto é, fixamos o tamanho da população ou, quando necessário, um valor aproximado e identificamos cada um pela sua posição.

{: .blockquote}
> Exemplo:
> E um grupo de 100 pessoas, precisamos de uma amostra de 20 pessoas. Então, faremos da seguinte forma:
>
> 1) Enumeramos as 100 pessoas de 1 a 5;
>
> 2) Realizamos o sorteio entre 1 e 5
>
> 3) Considerem que o número sorteado foi 3, então todas as pessoas com o número 3 farão parte da amostra.

#### Amostragem Probabilística Estratificada

Na Amostragem Probabilística Estratificada, os elementos são escolhidos proporcionalmente ao tamanho de cada estrato da população, isto é, a população é dividida em subgrupos, ou estratos, sem sobrepor elementos, e os elementos são tomados de cada estrato, de acordo com o tamanho de cada estrato.

É importante assegurar que as amostras dos diferentes estratos sejam independentes. As observações escolhidas num estrato não dependem das observações escolhidas nos outros estratos.

{: .blockquote}
> Exemplo:
>
> Num grupo de 100 pessoas, há 40 mulheres e 60 homens. Precisamos de uma amostra de 20 pessoas. Então, faremos da seguinte forma:
>
> 1) Separamos a amostra em dois estratos, 40 mulheres e 60 homens.
> 2) Para termos uma amostra de 20 pessoas, precisamos de 8 mulheres e 12 homens (o cálculo é feito de forma semelhante à Amostragem Proporcional).
> 3) Para cada estrato, podemos utilizar os métodos **Probabilísticos** anteriores (Amostragem Simples ou Amostragem Sistemática).
> 4) Por fim, somamos as 20 pessoas com a mesma representatividade da população.

#### Amostragem Probabilística por Conglomerados (por Clusters)

Na amostragem por Conglomerados, você tem acesso aos conglomerados, mas não tem acesso aos indivíduos que pertencem ao conglomerado. Então, o controle é feito por conglomerados e não por indivíduos.

Nessa amostragem, dividimos a população em conglomerados(clusters) e escolhemos os conglomerados de acordo com os métodos probabilísticos anteriores. Após essa escolha, os todos os elementos do conglomerado são escolhidos( por exemplo, entrevistados).

Um exemplo de situação onde isso é necessário é quando é impossível ou inviável criar um quadro de amostragem de uma população alvo, porque ela é espalhada geograficamente e o custo da recolha de dados é relativamente alto.

<div class="alert alert-info" role="alert">
    É importante destacar que a heterogeneidade do grupo é essencial para ter uma amostra por conglomerados. Além disso, os elementos dentro de cada grupo devem ser tão diversos como a população alvo!
</div>

{: .blockquote}
> Exemplo:
>
> Considere uma pesquisa que tem como objetivo conhecer o perfil dos
> adolescentes brasileiros. Observe que é inviável alcançar todos os
> adolescentes brasileiros, desta forma, pode-se dividir a população em
> estados ou regiões, por exemplo.
>
> Considere que o pesquisador escolheu agrupar esta população por
> estado. Até aqui está tudo certo, contudo, ainda assim, não será
> possível alcançar todos os adolescentes de cada estado, sendo assim,
> devem-se selecionar amostras dentro dos conglomerados.
>
> Para selecionar a amostra nos conglomerados, pode-se realizar uma das
> metodologias já estudadas ou aplicar novamente a amostragem
> probabilística por conglomerados, formando grupos menores, por
> exemplo, cidades. Assim a amostra é selecionada. O pesquisador que
> definirá o limite da divisão.
>
> Desta forma:
>
> 1) A população foi dividida em conglomerados (Estados).
>
> 2) Cada conglomerado foi dividido em outros menores, como cidades.
>
> 3) Seleciona-se uma amostra de conglomerados.
>
> 4) Observam-se todos os elementos dos conglomerados selecionados.
>
> 5) Conclui-se a característica da população.
