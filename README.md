# Estudo de Estatística

## Comandos úteis

### Construção da imagem

Para construir a imagem do contêiner, usamos o comando abaixo, na pasta do projeto.

```shell
docker build -t curso-probabilidade-estatistica .
```

### Execução do contêiner

Criar, dentro da pasta do projeto, a pasta `vendor/bundle`

Então, executar o contêiner com o seguinte comando:

```shell
docker run --rm -it -v "/d/repositorios/curso-probabilidade-estatistica:/srv/jekyll" -v "/d/repositorios/curso-probabilidade-estatistica/vendor/bundle:/usr/local/bundle" -p 4000:4000 -p 35729:35729 --name curso-probabilidade-estatistica curso-probabilidade-estatistica bash
```

### Pra executar o servidor de desenvolvimento

Executa o servidor do jekyll.

```shell
jekyll serve --watch --force-polling --livereload
```

Após a execução do `jekyll serve`, verifique, no Kitematic, qual a o IP para acessar o container ou execute, no terminal do host, o comando `docker-machine ip`. O endereço para acesso é [http://IP_DO_DOCKER_MACHINE/curso-probabilidade-estatistica]([http://IP_DO_DOCKER_MACHINE/curso-probabilidade-estatistica])

### Conectando num container que está rodando

```shell
docker exec -it curso-probabilidade-estatistica bash
```

## Referências

* [https://dev.to/michael/compile-a-jekyll-project-without-installing-jekyll-or-ruby-by-using-docker-4184](https://dev.to/michael/compile-a-jekyll-project-without-installing-jekyll-or-ruby-by-using-docker-4184)
* [https://programminghistorian.org/en/lessons/building-static-sites-with-jekyll-github-pages](https://programminghistorian.org/en/lessons/building-static-sites-with-jekyll-github-pages)
* [https://ddewaele.github.io/running-jekyll-in-docker/](https://ddewaele.github.io/running-jekyll-in-docker/)
* [https://github.com/envygeeks/jekyll-docker](https://github.com/envygeeks/jekyll-docker)


## Cores

- #eceff1 blue-grey lighten-5
- #cfd8dc blue-grey lighten-4
- #b0bec5 blue-grey lighten-3
- #90a4ae blue-grey lighten-2
- #78909c blue-grey lighten-1
- #607d8b blue-grey
- #546e7a blue-grey darken-1
- #455a64 blue-grey darken-2
- #37474f blue-grey darken-3
- #263238 blue-grey darken-4