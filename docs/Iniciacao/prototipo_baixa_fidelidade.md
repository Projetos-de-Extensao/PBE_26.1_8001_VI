---
id: prototipobaixa
title: Protótipo Baixa Fidelidade
---

## Introdução

<p align="justify">
Este protótipo de baixa fidelidade mostra o fluxo de um sistema de gestão de estágios para IBMEC, com telas claras e objetivas. A proposta é ser simples, funcional e direto, com foco nas funcionalidades essenciais para o estudante, o professor orientador e o supervisor da empresa.
</p>

## Estrutura do protótipo

- Autenticação e cadastro de usuários
- Cadastro e acompanhamento de estágio
- Envio e avaliação de relatórios
- Visualização do perfil e histórico

## Telas em PlantUML

### 1. Tela de Login

```plantuml
@startsalt
{+
<b>Plataforma de Gestão de Estágios - IBMEC</b>
==
Login
| "matricula@alunos.ibmec.edu.br"
Senha
| "********"
--
[ Entrar ]
[x] Lembrar-me
[ Esqueci minha senha ]
[ Criar conta ]
}
@endsalt
```

### 2. Tela de Cadastro de Usuário

```plantuml
@startsalt
{+
<b>Criar nova conta</b>
==
Nome completo
| "Maria Oliveira"
E-mail
| "maria@alunos.ibmec.edu.br"
Matrícula
| "202300123"
Curso
| "Engenharia"
Senha
| "********"
Confirmar senha
| "********"
--
[ Registrar ]
[ Voltar ]
}
@endsalt
```

### 3. Tela Recuperar Senha

```plantuml
@startsalt
{+
<b>Recuperar senha</b>
==
E-mail cadastrado
| "maria@alunos.ibmec.edu.br"
--
[ Enviar link de recuperação ]
Mensagem
| "Um link de redefinição foi enviado ao seu e-mail"
}
@endsalt
```

### 4. Dashboard do Aluno

```plantuml
@startsalt
{+
<b>Bem-vindo, Maria!</b>
==
Meus estágios:
{#
  Empresa      | Status       | Ação
  Ibmec Tech   | Em andamento | [ Ver detalhes ]
  Empresa Alfa | Aprovado     | [ Ver relatório ]
}
--
[ + Novo cadastro de estágio ]
}
@endsalt
```

### 5. Dashboard do Orientador / Supervisor

```plantuml
@startsalt
{+
<b>Minhas supervisões</b>
==
Estagiários:
{#
  Estudante      | Empresa      | Relatórios
  João Silva     | Ibmec Tech   | 2 pendentes
  Ana Pereira    | Empresa Beta | 1 pendente
}
--
[ Avaliar relatório ]
[ Ver histórico ]
}
@endsalt
```

### 6. Formulário de Estágio

```plantuml
@startsalt
{+
<b>Cadastrar estágio</b>
==
Tipo
| "Obrigatório" [x]  "Não obrigatório" [ ]
Empresa
| "Ibmec Tech"
Supervisor
| "Fábio Souza"
Orientador
| "Prof. Lúcia"
Início
| "01/05/2026"
Término
| "30/11/2026"
Carga semanal
| "30h"
Atividades
| "Acompanhamento de atividades administrativas"
--
[ Salvar ]
[ Cancelar ]
}
@endsalt
```

### 7. Tela de Detalhes do Estágio

```plantuml
@startsalt
{+
<b>Detalhes do estágio</b>
==
Estudante
| "Maria Oliveira"
Empresa
| "Ibmec Tech"
Supervisor
| "Fábio Souza"
Orientador
| "Prof. Lúcia"
Carga horária
| "18h / 30h"
Status
| "Em andamento"
Documentos
| "TCE" "Relatório 01"
--
[ Enviar relatório ]
[ Editar estágio ]
[ Finalizar estágio ]
}
@endsalt
```

### 8. Tela de Envio de Relatório

```plantuml
@startsalt
{+
<b>Novo relatório</b>
==
Título
| "Relatório semanal 01"
Período
| "01/05/2026 - 07/05/2026"
Atividades
| "Atualização do TCE e reunião com supervisor"
Anexo
| "relatorio_semana01.pdf"
--
[ Enviar ]
[ Salvar como rascunho ]
Mensagem
| "Relatório enviado para avaliação"
}
@endsalt
```

### 9. Tela de Avaliação de Relatório

```plantuml
@startsalt
{+
<b>Avaliar relatório</b>
==
Estudante
| "Maria Oliveira"
Estágio
| "Ibmec Tech"
Período
| "01/05/2026 - 07/05/2026"
Anexo
| "relatorio_semana01.pdf"
--
[ Aprovar ]
[ Solicitar correção ]
Comentário
| "Revisar descrição de atividades e anexar comprovante"
}
@endsalt
```

### 10. Tela de Perfil do Usuário

```plantuml
@startsalt
{+
<b>Meu perfil</b>
==
Nome
| "Maria Oliveira"
E-mail
| "maria@alunos.ibmec.edu.br"
Tipo
| "Estudante"
Curso
| "Engenharia"
--
[ Editar perfil ]
[ Alterar senha ]
[ Sair ]
}
@endsalt
```

## Visão simplificada do fluxo em PlantUML

```plantuml
@startuml
actor Estudante
actor ProfessorOrientador
actor SupervisorEmpresa

Estudante -> Login : acessar
ProfessorOrientador -> Login : acessar
SupervisorEmpresa -> Login : acessar

Login -> DashboardEstudante : redirecionar
Login -> DashboardAvaliador : redirecionar

DashboardEstudante -> EstagioForm : cadastrar estágio
DashboardEstudante -> EstagioDetalhes : ver estágio
EstagioDetalhes -> RelatorioForm : enviar relatório
RelatorioForm -> Avaliacao : aguardar avaliação

DashboardAvaliador -> Avaliacao : avaliar relatório
Avaliacao -> EstagioDetalhes : atualizar status

@enduml
```

## Observações importantes

- O protótipo privilegia a clareza das ações e a hierarquia de informações.
- As telas foram desenhadas para facilitar o trabalho do estudante, do orientador e do supervisor.
- O fluxo de aprovação de relatórios é central para a conformidade do estágio.

## Conclusão

<p align="justify">
O documento agora apresenta um protótipo de baixa fidelidade mais enxuto, organizado e fácil de entender. Ele mantém o foco nas funcionalidades essenciais e melhora a leitura em relação ao modelo inicial.
</p>

## Autor(es)

| Data     | Versão | Descrição                                   | Autor(es) |
| -------- | ------- | ------------------------------------------- | --------- |
| 16/04/2026 | 1.1   | Protótipo de baixa fidelidade revisado | Caio Cunha Dantas |
