---
id: documento_de_arquitetura
title: Documento de Arquitetura
---
# Documento de Arquitetura de Software (DAS)

# Sistema de Gestão de Estágios

# Introdução

## Proposta

<p align = "justify">
Este documento apresenta uma visão geral da arquitetura do Sistema de Gestão de Estágios,
utilizando diferentes visões arquiteturais para destacar aspectos relevantes do sistema, e
registra as principais decisões arquiteturais adotadas.
</p>

## Escopo

<p align = "justify">
A aplicação tem o objetivo de fornecer uma API REST para gestão do ciclo de vida de estágios
acadêmicos: cadastro de estudantes, empresas, professores orientadores e supervisores; registro
de estágios; e envio/validação de relatórios.
</p>

## Definições, Acrônimos e Abreviações

- **MVT** – Model-View-Template, padrão arquitetural do Django.
- **DRF** – Django REST Framework.
- **JWT** – JSON Web Token, mecanismo de autenticação stateless.
- **TCE** – Termo de Compromisso de Estágio.
- **API** – Application Programming Interface.

## Visão Geral

<p align = "justify">
O Documento de Arquitetura de Software (DAS) traz uma visão geral da arquitetura do sistema.
São abordadas as seguintes visões:
</p>

- Caso de Uso;
- Lógica;
- Implantação;
- Implementação;
- Dados;

# Representação Arquitetural

## Cliente-Servidor

<p align = "justify">
O sistema adota o modelo Cliente-Servidor. O back-end expõe uma API REST consumida por clientes
externos (web ou mobile). Internamente, o Django organiza-se no padrão MVT, adaptado para API
com o DRF.
</p>

Cliente (Frontend):

- Consome a API REST via HTTP (JSON), autenticando-se por JWT. (Fora do escopo deste projeto.)

Servidor (Backend - Django + DRF):

- **URLs/Router**: roteamento das requisições para os ViewSets.
- **ViewSet (View)**: recebe a requisição, aplica permissões, paginação, filtros e throttling.
- **Serializer**: validação e (de)serialização dos dados de entrada/saída.
- **Model**: persistência e regras de domínio sobre o banco de dados (ORM do Django).

# Objetivos de Arquitetura e Restrições

## Objetivos

<p align = "justify">

**Segurança:**
   - Autenticação via JWT; SECRET_KEY e configurações sensíveis em variáveis de ambiente; diretivas de segurança HTTP (HSTS, cookies seguros, X-Frame-Options) configuráveis por ambiente.

**Persistência:**
   - ORM do Django; SQLite em desenvolvimento e banco configurável via `DATABASE_URL` (ex.: PostgreSQL) em produção.

**Privacidade:**
   - Permissões por endpoint (IsAuthenticated); throttling para mitigar abuso; tratamento de dados pessoais alinhado à LGPD (ver documento de LGPD).

**Desempenho:**
   - Otimização de consultas com `select_related`/`prefetch_related` (evita N+1); paginação padrão nas listagens.

**Reusabilidade:**
   - ViewSets e Routers do DRF; serializers reutilizáveis; documentação automática via OpenAPI/Swagger.
</p>

## Restrições

<p align = "justify">

Portabilidade: API REST consumível por qualquer cliente HTTP.

Acesso à internet: a aplicação requer conexão com a internet.

</p>

## Ferramentas Utilizadas

- **Python 3.12**: linguagem de programação.
- **Django 4.2.11**: framework web.
- **Django REST Framework 3.14**: construção da API REST.
- **djangorestframework-simplejwt**: autenticação JWT.
- **django-cors-headers**: configuração de CORS.
- **django-filter**: filtragem dos endpoints.
- **drf-spectacular**: documentação OpenAPI/Swagger.
- **python-decouple / dj-database-url**: configuração por variáveis de ambiente.
- **SQLite / PostgreSQL**: banco de dados.

# Visão de Caso de Uso

<p align = "justify">
Os casos de uso centrais são: Cadastrar Estágio, Enviar Relatório, Avaliar Relatório, Validar
Estágio e Consultar Status. O diagrama completo está em
<a href="./casos_de_uso/">Casos de Uso</a>.
</p>

# Visão Lógica

<p align = "justify">
A camada lógica organiza-se em torno das entidades de domínio (Estudante, Empresa,
ProfessorOrientador, SupervisorEmpresa, Estagio, Relatorio) e das entidades de conteúdo
(Content, Playlist). Cada entidade possui Model, Serializer e ViewSet correspondentes.
</p>

# Visão de Implantação

<p align = "justify">
A aplicação é servida por um servidor WSGI (ex.: Gunicorn/uWSGI) atrás de um proxy reverso
(ex.: Nginx). Em produção, recomenda-se PostgreSQL via <code>DATABASE_URL</code> e HTTPS com as
diretivas de segurança habilitadas por variáveis de ambiente.
</p>

# Visão de Implementação

## Visão Geral

<p align = "justify">
O código está organizado no app <code>content_app</code> (models, serializers, views, urls,
admin, tests) e no projeto <code>streaming_platform</code> (settings, urls raiz, wsgi/asgi).
</p>

# Visão de Dados

## Modelo Entidade Relacionamento (MER)

#### Entidades e Relacionamentos:

- **Estudante** (1) — (N) **Estagio**
- **Empresa** (1) — (N) **Estagio**
- **Empresa** (1) — (N) **SupervisorEmpresa**
- **ProfessorOrientador** (1) — (N) **Estagio**
- **SupervisorEmpresa** (1) — (N) **Estagio**
- **Estagio** (1) — (N) **Relatorio**
- **User** (1) — (N) **Content** / **Playlist**
- **Playlist** (N) — (N) **Content**

## Diagrama Entidade Relacionamento (DER)

Ver o [Diagrama de Classes](./diagrama_de_classes/).

# Tamanho e Desempenho

<p align = "justify">
As listagens utilizam paginação (20 itens por página por padrão) e consultas otimizadas para
evitar o problema de N+1. O throttling limita requisições anônimas (100/h) e autenticadas
(1000/h).
</p>

# Qualidade

<p align = "justify">
A qualidade é apoiada por testes automatizados (models, serializers e endpoints), validações nos
serializers e documentação automática da API (Swagger/Redoc).
</p>

# Referências Bibliográficas

> Django Software Foundation. **Django Documentation**. https://docs.djangoproject.com/. Acesso em 09/06/2026.

> Encode. **Django REST Framework**. https://www.django-rest-framework.org/. Acesso em 09/06/2026.

# Histórico de Versão

| Data       | Versão | Descrição                                                       | Autor(es)        |
| ---------- | ------- | --------------------------------------------------------------- | ---------------- |
| 09/06/2026 | 1.0     | Preenchimento do DAS com a arquitetura real do sistema          | Equipe PBE 8001  |
