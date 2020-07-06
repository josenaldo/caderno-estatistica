---
title: Aula 003
description: Técnicas de Amostragem e Coleta de Dados
permalink: aulas/aula-003
videos: NvqHnM3TucE vcTQCIfz9_M
---

A pesquisa científica, observacional ou experimental, busca dados sobre a tese a ser comprovada e estabelece comparações entre grupos com características distintas.

Falando de forma simplória, ela verifica:

- O que?
  - Características a serem observadas - variáveis
- Quem:
  - Elementos a serem pesquisados - população
- Como
  - O instrumento de coleta de dados - questionário ou entrevista estruturada

E como a estatística interage com essa pesquisa?

{% include imagem.html
    url="assets/images/aula-001/interacao-entre-estatistica-e-a-pesquisa-cientifica.png"
    description="Interação entre estatística e a pesquisa científica" %}

A primeira pergunta de um pesquisador, no início da pesquisa, é: serão coletados os dados de toda uma população ou apenas uma parcela representativa dessa população?

Nesse ponto, o pesquisador deve observar que se coletar uma amostra grande demais, haverá desperdício de tempo, dinheiro e trabalho. Contudo, coletar uma amostra pequena demais também pode gerar desperdício de tempo, dinheiro e trabalho.

Mas afinal, o que é população? E o que é amostra?

## População e Amostra

**População** é todo o conjunto de elementos que têm em comum uma determinada característica.

Exemplo: população de habitantes do Brasil, todos os torcedores do Íbis futebol Clube, todos os smartphones do estado da Bahia.

Já **amostra**, é um subconjunto de elementos da população, desde que esse subconjunto seja não vazio e com número de elementos menor que o número de elementos da população. Ou seja: $$0 < n(A) < n(P)$$, onde:

- $$n(A)$$ = número de elementos da amostra
- $$n(P)$$ = número de elementos da população

{% include imagem.html
    url="assets/images/aula-003/populacao-e-amostra.png"
    description="População e Amostra" %}

Definir o tamanho da amostra é uma das principais dificuldades do pesquisador. O tamanho da amostra é independente do tamanho da população e não determina se a amostra é boa ou ruim. O que mais importa, na hora de escolher o tamanho de uma amostra, é o grau de similaridade dessa amostra com a população.

O cálculo do tamanho da amostra deve levar em consideração os seguintes fatores:

- nível de confiança
- a precisão desejada para os resultados obtidos
- a variabilidade dos dados (o quanto estão dispersos em relação À característica em estudo)
- o custo

Na hora de escolher uma amostra ou coletar os dados, o pesquisador deve tomar cuidado para não fazer uma coleta tendenciosa. Se essa coleta for tendenciosa, seja por descuido, seja propositalmente, é dito que a amostra está viciada.

Para evitar isso, o primeiro cuidado é garantir que a amostra seja representativa de todos os perfis da população. Ou seja, quanto mais parecida com a população, melhor a amostra.

## Técnicas de Amostragem e Coleta de Dados

{% include imagem.html
    url="assets/images/aula-003/tipos-de-amostragem.jpeg"
    description="Tipos de Amostragem" %}

Na classificação geral do levantamento de coleta de amostra, temos duas possibilidades de coletas:

- Não Probabilística
- Probabilística

### Coleta Não Probabilística

Também chamada de Coleta Não Aleatória. Ao realizar esse tipo de coleta, o pesquisador escolhe, de maneira deliberada, os elementos da amostra. Para isso, ele se utiliza de seus próprios critérios.

Esse tipo de amostra é classificada em 3 tipos: intencional, voluntária e acidental.

O problema desse tipo de amostragem é que não se conhece a probabilidade de cada unidade amostral pertencer à amostra. Ou seja, não se sabe o grau de similaridade da amostra com a população. Por isso essas técnicas não garantem a ausência de vícios.

Dessas forma, não há problema em se usar esse tipo de técnica, desde que isso seja deixado claro no estudo e que os resultados limitem-se apenas ao grupo escolhido e não a toda população.

### Coleta Probabilística

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
> 2) Para termos uma amostra de 20 pessoas, precisamos de 8 mulheres e 12 homens.
> 3) Para cada estrato, podemos utilizar os métodos anteriores.
> 4) Por fim, somamos as 20 pessoas com a mesma representatividade da população.

#### Amostragem Probabilística por Conglomerados (por Clusters)

Na Amostragem Probabilística Estratificada, os elementos da amostra são escolhidos aleatoriamente, de forma natural, por grupos (clusters). esse método se faz necessário em situações nas quais é impossível ou inviável criar um quadro de amostragem de uma população alvo, porque ela é espalhada geograficamente e o custo da recolha de dados é relativamente alto.

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

### Coleta De Dados

{% include imagem.html
    url="assets/images/aula-003/tipos-de-coleta.jpeg"
    description="Tipos de Coletas" %}
Existe duas formas de coletarmos dados de uma pesquisa: a direta e a indireta.

- Coleta Indireta
  - É feita a partir dos dados já coletados anteriormente por meio da coleta direta ou do conhecimento de fenômenos relacionados ao objeto de estudo como, por exemplo, citando uma pesquisa já realizada.
- Coleta Direta
  - É aquela realizada pelo próprio pesquisador, utilizando os diferentes meios disponíveis – questionários, entrevistas, levantamento de registros (nascimentos, óbitos, notas fiscais, impostos, etc.). A coleta direta pode ser classificada de três formas: contínua, periódica ou ocasional.

#### Tipos de Coleta Direta

- Coleta Direta Contínua
  - Como o próprio nome já sugere, a coleta direta é classificada como contínua quando é feita de forma continuada, como registros de casamentos, nascimentos e óbitos, importação e exportação de mercadorias, prontuários, frequência de alunos às aulas, etc.
- Coleta Direta Periódica
  - Quando a coleta é feita em intervalos constantes de tempo, ela é classificada como periódica, por exemplo, os censos (10 em 10 anos),avaliações bimestrais dos alunos, ENADE - Exame Nacional de Desempenho dos Estudantes – com periodicidade máxima trienal para cada área do conhecimento, etc.
- Coleta Direta Ocasional
  - Quando a coleta é feita em determinada situação pontual, para atender a um objetivo específico, essa coleta é classificada como ocasional, por exemplo, uma pesquisa para traçar o perfil de comunidade e suas demandas por formação profissional, superpopulação de algas em praia, pesquisa de um produto no mercado, etc.

## Tabelas Estatísticas

Ao organizar os dados da pesquisa, a primeira etapa é organizar um ROL.
Nessa etapa, organizamos os dados por ordem de valor, de maneira crescente ou decrescente, de acordo.

Após a organização desses dados no ROL, podemos gerar uma nova tabela, compacta, com as frequências dos dados.

Mas o que é uma tabela?

<div class="alert alert-info" role="alert">
A Associação Brasileira de Normas Técnicas (ABNT), através da norma NBR 14724:2011, conceitua tabela como forma não discursiva de apresentar informações das quais o dado numérico se destaca como informação central.
</div>

Em outras palavras, tabela é um quadro que resume um conjunto de dados dispostos segundo linhas e colunas de maneira organizada (sistemática).

{% include imagem.html
    url="assets/images/aula-003/exemplo-de-tabela.png"
    description="Exemplo de tabela" %}

Segundo a ABNT, uma tabela tem a seguinte estrutura:

{% include imagem.html
    url="assets/images/aula-003/estrutura-da-tabela.png"
    description="Estrutura de tabela" %}

Sendo:

- **Topo** - Espaço superior de uma tabela destinado ao seu número e ao seu
título.
- **Cabeçalho** - Espaço superior do centro de uma tabela destinado à indicação do conteúdo das colunas.
- **Centro** - Espaço central de uma tabela destinado à moldura, aos dados numéricos e aos termos necessários à sua compreensão.
- **Rodapé** - Espaço inferior de uma tabela destinado à fonte, à nota geral e à nota específica.

### Classificação De Tabelas

Dependendo dos dados apresentados, uma tabela pode ser classificada em:

- Série histórica
- Série específica ou categórica
- Série geográfica ou tabelas de dupla entrada.

#### Série Histórica

Também conhecidas como temporais ou cronológicas, consistem em tabelas em que o elemento variável é o fator cronológico.

{% include imagem.html
    url="assets/images/aula-003/classificacao-de-tabela-serie-historica.png"
    description="Série Histórica" %}

#### Série Específica Ou Categórica

Descreve os valores da variável em determinado tempo e local, discriminados segundo especificações ou categorias.

{% include imagem.html
    url="assets/images/aula-003/classificacao-de-tabela-serie-categorica.png"
    description="Série Categórica" %}

#### Série Geográfica

Também conhecida como espacial, territorial ou de localização, descreve os valores da variável, em determinado tempo, discriminados segundo a localização geográfica da variável.

{% include imagem.html
    url="assets/images/aula-003/classificacao-de-tabela-serie-geografica.png"
    description="Série Geográfica" %}

#### Tabelas De Dupla Entrada

Útil para mostrar dois ou mais tipos de dado sobre um item. Deve ser lida na vertical e na horizontal simultaneamente para que as linhas e as colunas sejam relacionadas.

{% include imagem.html
    url="assets/images/aula-003/classificacao-de-tabela-serie-dupla-entrada.png"
    description="Tabela de Dupla Entrada" %}