# MkDocs

## Papel do site no projeto

O site em MkDocs funciona como a camada principal de apresentacao da documentacao do projeto. Em vez de ser apenas um artefato auxiliar, ele organiza os documentos em uma navegacao unica e facilita tanto a revisao interna quanto a apresentacao externa.

## Estrutura atual

- `mkdocs.yml`: configuracao principal do site
- `docs/`: paginas e ativos da documentacao
- `docs/assets/`: imagens e materiais de apoio
- `docs/css/extra.css`: customizacao visual adicional

## Comandos principais

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Executar localmente:

```bash
mkdocs serve
```

Gerar a versao estaticamente:

```bash
mkdocs build
```

Publicar no GitHub Pages:

```bash
mkdocs gh-deploy
```

## Observacao importante

O comando correto para publicacao e `mkdocs gh-deploy`. Se aparecer `gh-depoly`, trata-se apenas de um erro de digitacao.

## Objetivo desta organizacao

Com a documentacao estruturada em site, fica mais facil transformar o conteudo em roteiro de apresentacao, porque a navegacao ja separa contexto, proposta, artefatos e apoio.
