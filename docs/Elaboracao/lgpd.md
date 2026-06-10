---
id: lgpd
title: Conformidade com a LGPD
---

# Conformidade com a LGPD

Este documento descreve como o Sistema de Gestão de Estágios trata dados pessoais, em
conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).

## Dados Pessoais Tratados

| Entidade | Dados pessoais | Sensível? |
| -------- | -------------- | --------- |
| Estudante | nome, matrícula, curso | Não |
| Empresa | razão social, CNPJ | Não (dado de pessoa jurídica) |
| Professor Orientador | nome | Não |
| Supervisor da Empresa | nome | Não |
| Usuário (auth) | username, e-mail, senha (hash) | Não |

O sistema **não** coleta dados sensíveis (origem racial, saúde, biometria etc.).

## Bases Legais de Tratamento

- **Execução de contrato / obrigação legal** (art. 7º, II e V): o tratamento dos dados de
  estudantes e estágios decorre da relação acadêmica e das exigências legais de estágio
  (Lei nº 11.788/2008 — Lei do Estágio).
- **Legítimo interesse** (art. 7º, IX): acompanhamento e validação dos estágios pela
  instituição.

## Princípios Aplicados

- **Finalidade**: os dados são usados exclusivamente para gestão de estágios.
- **Adequação e necessidade (minimização)**: coletam-se apenas os dados estritamente
  necessários ao processo.
- **Segurança**: autenticação JWT, segredos em variáveis de ambiente, controle de acesso por
  permissões e throttling.
- **Transparência**: este documento e a documentação da API descrevem o tratamento realizado.

## Direitos dos Titulares

Os titulares têm direito a confirmação, acesso, correção, anonimização, portabilidade e
eliminação de seus dados (art. 18). Operacionalmente:

- **Acesso/correção**: via endpoints REST (`GET`/`PATCH`) ou solicitação à coordenação.
- **Eliminação**: via `DELETE` nos respectivos endpoints, respeitada a retenção legal.

## Retenção e Eliminação

- Os dados de estágio são retidos enquanto durar a obrigação legal/acadêmica.
- Encerrado o prazo de retenção, os registros devem ser eliminados ou anonimizados.

## Medidas Técnicas e Organizacionais

- Acesso restrito a usuários autenticados.
- Senhas armazenadas com hash (PBKDF2, padrão do Django).
- Configurações de segurança HTTP habilitáveis em produção (HTTPS, HSTS, cookies seguros).
- Recomenda-se, em produção, manter logs de auditoria de acesso e um encarregado (DPO)
  designado.

## Melhorias Recomendadas (Roadmap)

- Registro de logs de auditoria de acesso a dados pessoais.
- Rotina automatizada de anonimização após o prazo de retenção.
- Endpoint de exportação de dados do titular (portabilidade).

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 09/06/2026 | 1.0 | Criação do documento de conformidade com a LGPD | Equipe PBE 8001 |
