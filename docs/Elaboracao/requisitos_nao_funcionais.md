---
id: requisitos_nao_funcionais
title: Requisitos Não Funcionais
---

# Requisitos Não Funcionais (RNF)

Os requisitos não funcionais descrevem atributos de qualidade do Sistema de Gestão de Estágios.
Cada item indica como é atendido na implementação atual.

## Segurança

| ID | Requisito | Como é atendido |
| -- | --------- | --------------- |
| RNF-01 | Credenciais e segredos não devem ser versionados | `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL` em variáveis de ambiente (`python-decouple`); `.env` no `.gitignore` |
| RNF-02 | Autenticação stateless e segura | Autenticação via JWT (`djangorestframework-simplejwt`), com tokens de acesso (60 min) e refresh (1 dia) |
| RNF-03 | Operações de escrita restritas a usuários autenticados | Permissões `IsAuthenticated` / `IsAuthenticatedOrReadOnly` nos endpoints |
| RNF-04 | Proteção de transporte em produção | Diretivas configuráveis: `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_HSTS_SECONDS`, `X_FRAME_OPTIONS` |
| RNF-05 | Controle de origens (CORS) | `django-cors-headers` com `CORS_ALLOWED_ORIGINS` por ambiente |

## Desempenho

| ID | Requisito | Como é atendido |
| -- | --------- | --------------- |
| RNF-06 | Listagens não devem retornar todos os registros de uma vez | Paginação padrão (`PageNumberPagination`, 20 itens/página) |
| RNF-07 | Evitar consultas redundantes (N+1) | `select_related`/`prefetch_related` nos ViewSets |
| RNF-08 | Limitar abuso e força bruta | Throttling: 100/h (anônimo) e 1000/h (autenticado) |

## Confiabilidade e Integridade

| ID | Requisito | Como é atendido |
| -- | --------- | --------------- |
| RNF-09 | Validação de dados de entrada | Validações nos serializers (CNPJ, matrícula, carga horária, supervisor x empresa) |
| RNF-10 | Consistência referencial | Chaves estrangeiras com `on_delete=CASCADE` e campos `unique` (matrícula, CNPJ) |
| RNF-11 | Restrição de valores de domínio | `choices` em campos de status e tipo |

## Manutenibilidade

| ID | Requisito | Como é atendido |
| -- | --------- | --------------- |
| RNF-12 | Código testável e testado | Suíte de testes (models, serializers e endpoints) |
| RNF-13 | API evolutiva sem quebrar clientes | Versionamento por prefixo de URL (`/api/v1/`) |
| RNF-14 | Documentação sempre atualizada | OpenAPI/Swagger automático via `drf-spectacular` (`/api/docs/`, `/api/redoc/`) |

## Portabilidade

| ID | Requisito | Como é atendido |
| -- | --------- | --------------- |
| RNF-15 | Banco de dados configurável por ambiente | `dj-database-url` via `DATABASE_URL` (SQLite em dev, PostgreSQL em produção) |
| RNF-16 | Consumo por qualquer cliente HTTP | API REST com respostas em JSON |

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 09/06/2026 | 1.0 | Criação do documento de requisitos não funcionais | Equipe PBE 8001 |
