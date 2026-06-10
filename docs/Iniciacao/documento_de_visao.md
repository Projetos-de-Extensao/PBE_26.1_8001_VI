---
id: documento_de_visao
title: Documento de Visão
---
## Introdução

<p align = "justify">
O propósito deste documento é fornecer uma visão geral do projeto desenvolvido na disciplina
Projeto Back-End (IBM8936) do IBMEC. São descritas, de forma resumida, as principais
funcionalidades, os usuários, o problema abordado e os objetivos da equipe para o
<strong>Sistema de Gestão de Estágios</strong>.
</p>

## Descrição do Problema

<p align = "justify">
O processo de acompanhamento de estágios em instituições de ensino é frequentemente
fragmentado: documentos (como o Termo de Compromisso de Estágio - TCE) circulam por e-mail,
relatórios são enviados em formatos diversos e o controle de prazos e status depende de
planilhas manuais. Isso gera retrabalho, perda de informações e dificuldade de
acompanhamento por parte de estudantes, professores orientadores, supervisores e coordenação.
</p>

### Problema

Dificuldade em gerenciar, organizar e acompanhar o ciclo de vida dos estágios (cadastro,
documentação, envio e validação de relatórios) de forma centralizada e auditável.

### Impactados

Estudantes, Professores Orientadores, Supervisores das Empresas e a Coordenação de Estágios.

### Consequência

A ausência de uma plataforma centralizada provoca atrasos na validação de estágios, perda de
documentos, inconsistência de dados e baixa rastreabilidade do andamento de cada estágio.

### Solução

Disponibilizar uma API REST que centralize o cadastro de estudantes, empresas, supervisores e
professores orientadores, o registro de estágios (obrigatórios e não obrigatórios) e o
envio/validação de relatórios periódicos, com controle de status em cada etapa.

## Objetivos

<p align = "justify">
O objetivo da equipe é fornecer um back-end robusto, seguro e documentado que automatize a
gestão de estágios, padronize o fluxo de relatórios e ofereça transparência sobre o status de
cada estágio para todos os envolvidos.
</p>

## Descrição do Usuário

<p align = "justify">
Os usuários do sistema são:
</p>

- **Estudante**: cadastra seu estágio e envia relatórios periódicos.
- **Professor Orientador**: acompanha e avalia os relatórios do estudante.
- **Supervisor da Empresa**: acompanha o estágio e fornece feedback sobre o estudante.
- **Coordenação**: valida os estágios e monitora a conformidade institucional.

## Recursos do produto

### Cadastro de Estágio

<p align = "justify">
Permite registrar um estágio vinculando estudante, empresa, professor orientador e supervisor,
informando tipo (obrigatório/não obrigatório) e carga horária.
</p>

### Gestão de Relatórios

<p align = "justify">
Permite o envio de relatórios vinculados a um estágio, com controle de status
(pendente, aprovado, reprovado) pelo professor orientador.
</p>

### Consulta de Status

<p align = "justify">
Permite que os envolvidos consultem o andamento de estágios e relatórios, com filtros por
status, empresa, estudante e período.
</p>

### Validação de Estágio

<p align = "justify">
Permite que a Coordenação valide e altere o status do estágio
(em andamento, concluído, cancelado).
</p>

## Restrições

<p align = "justify">
A aplicação é um back-end (API REST); a interface de consumo (web/mobile) está fora do escopo
deste projeto. O sistema depende de conexão com a internet e requer autenticação para todas as
operações de escrita.
</p>

## Referências Bibliográficas

> Django Software Foundation. **Django Documentation**. Disponível em: https://docs.djangoproject.com/. Acesso em 09/06/2026.

> Encode. **Django REST Framework**. Disponível em: https://www.django-rest-framework.org/. Acesso em 09/06/2026.

## Versionamento
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 09/06/2026 | 1.0 | Preenchimento do documento com o domínio de gestão de estágios | Equipe PBE 8001 |
