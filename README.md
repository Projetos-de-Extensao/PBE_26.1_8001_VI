# Projeto Back-End 

Grupo:

Henrique Cals, Guilherme Pinon, Caio Cunha, Henrique Mundy, João Pedro Sampaio e Pedro Paulo


Apresentação:

https://liveestacio-my.sharepoint.com/:p:/g/personal/202501537839_alunos_ibmec_edu_br/IQB8UMz0nByBS7uPJAoZ99wRASNVzPJvIqZhxM6cfmXu6qw?e=l55hlh

**Código da Disciplina**: IBM8936<br>

## Sobre 
Descreva o seu projeto em linhas gerais. 

Back-end desenvolvido na disciplina de Projeto Back-End do IBMEC, construído em Python com foco em arquitetura limpa e boas práticas de desenvolvimento.

## Instalação 
**Linguagens**: Python, Django<br>
**Tecnologias**: Github, Visual Studio Code<br>
 os pré-requisitos para rodar o seu projeto são UX, Engenharia de Dados, POO.

 # Levantamento de Requisitos
 
  ### Requisitos Funcionais (RF)
   ### Contas
   RF01 -> O sistema deve permitir o usuário criar contas. <br>
   RF02 -> O sistema deve validar os dados informados no cadastro. <br>
   RF03 -> O sistema deve criptografar dados sensíveis do usuário. <br>
   RF04 -> O sistema deve enviar e-mail de verificação com link de confirmação. <br>
   RF05 -> O sistema deve permitir login no sistema. <br>
   RF06 -> O sistema deve permitir alteração dos dados da conta. <br>
   RF07 -> O sistema deve permitir recuperação de senha. <br>    
   RF08 -> O sistema deve realizar exclusão lógica de contas. <br>
   RF09 -> O sistema deve permitir visualização dos dados da conta. <br>


   ### Perfis
   RF10 -> O sistema deve permitir a edição de perfis. <br>
   RF11 -> O sistema deve permitir pesquisar perfis. <br>
   RF12 -> O sistema deve permitir ver perfis. <br>
   RF13 -> O sistema deve permitir seguir usuários. <br>
   RF14 -> O sistema deve permitir deixar de seguir usuários. <br>


   ### Postagens Públicas
   RF15 -> O sistema deve permitir a criação de postagens públicas. <br>
   RF16 -> O sistema deve permitir excluir postagens. <br>
   RF17 -> O sistema deve permitir interagir com postagens. <br>
   RF18 -> O sistema deve permitir ver postagens. <br>


   ### Mensagens Privadas
   RF19 -> O sistema deve permitir enviar mensagens privadas. <br>
   RF20 -> O sistema deve permitir excluir mensagens. <br>
   RF21 -> O sistema deve permitir ver mensagens. <br>


   ### Albuns
   RF22 -> O sistema deve permitir criar e gerenciar álbuns. <br>


   ### Blogs
   RF23 -> O sistema deve permitir criar e gerenciar blogs. <br>


   ### Grupos
   RF22 -> O sistema deve permitir criar e gerenciar grupos. <br>


   ### Autenticação de conta
   RF25 -> O sistema deve autenticar usuários com e-mail e senha. <br>
   RF26 -> O sistema deve redirecionar o usuário após o login. <br>
   RF27 -> O sistema deve identificar o primeiro acesso. <br>
   RF28 -> O sistema deve enviar mensagens de erros quando necessário. <br>




   ### Requisitos Não Funcionais (RNF)
   RNF01 -> O sistema deve dar segurança pra dados com criptografias. <br>
   RNF02 -> O sistema deve validar as entradas de dados. <br>
   RNF03 -> O sistema deve verificar se e-mais com link de verificação estão válidos. <br>
   RNF04 -> O sistema deve enviar e-mails automaticamente. <br>
   RNF05 -> O sistema deve ter bons desempenhos operacionais. <br>
   RNF06 -> O sistema deve permitir assegurar a integridade dos dados. <br>
   RNF07 -> O sistema deve ter interface intuitiva. <br>    




   
 # Casos de Uso de forma narrativa

## Caso de Uso 1 - Criação de Conta <br>
* Atores - Aluno, Sistema  <br>
  * Descrição - Aluno poder cirar uma conta.  <br>

  * Pré-Condição
     --> Nenhuma.

    * Fluxo principal: <br>
      1 - O aluno fornece e-mail, cria senha e confirma; <br>
      2 - O sistema valida os dados; <br>
      3 - O sistema criptografa os dados; <br>
      4 - O sistema armazena os dados; <br>
      5 - O sistema gera link 2-fatores; <br>
      6 - O sistema envia o link por e-mail; <br>
      7 - O aluno acessa o link; <br>
      8 - O sistema confirma o cadastro. <br>
      9 - O sistema redireciona o aluno pro login. <br>

        * Fluxo Alternativo: <br>
           --> 2.1) O e-mail é inválido <br>  |-- Gera erro e solicitação de correção; <br>
           --> 2.2) Senha fora do padrão <br>  |-- Gera erro e splicitação de correção.<br>
           --> 7.1) Link expirado <br>  |-- Sistema solicita novo cadastro.<br>



## Caso de Uso 2 - Login <br>
* Atores - Aluno, Sistema  <br>
  * Descrição - Aluno poder acessar o sistema.  <br>

  * Pré-Condição
     --> Realizar cadastro.

    * Fluxo principal: <br>
      1 - O aluno fornece e-mail e senha; <br>
      2 - O sistema autentica os dados; <br>
      3 - O sistema leva pra página inicial; <br>
   
        * Fluxo Alternativo: <br>
           --> 2.1) Dados inválidos <br>  |-- Gera erro e solicitação de correção; <br>
           --> 3.1) Primeiro acesso <br>  |-- Leva pra criação de perfil.<br>



## Caso de Uso 3 - Seguir Usuário <br>
* Atores - Aluno  <br>
  * Descrição - Aluno poder seguir outro perfil.  <br>

  * Pré-Condição
     --> Ter perfil criado.

    * Fluxo principal: <br>
      1 - O aluno acessa um perfil; <br>
      2 - O aluno clica em "Seguir"; <br>
      3 - O sistema registra; <br>
      4 - O sistema atualiza os seguidores; <br>



## Caso de Uso 4 - Criar postagem <br>
* Atores - Aluno  <br>
  * Descrição - Aluno poder postar conteúdo.  <br>

  * Pré-Condição
     --> Ter perfil criado.

    * Fluxo principal: <br>
      1 - O aluno acessa a área de posts; <br>
      2 - O aluno insere conteúdo; <br>
      3 - O aluno confirma a postagem; <br>
      4 - O sistema armazena; <br>
      5 - O sistema disponibiliza publicamente; <br>



## Caso de Uso 5 - Enviar DM <br>
* Atores - Aluno  <br>
  * Descrição - Aluno poder enviar mensagens privadas.  <br>

  * Pré-Condição
     --> Ter perfil criado.

    * Fluxo principal: <br>
      1 - O aluno seleciona para quem quer mandar mensagem; <br>
      2 - O aluno escreve a mensagem; <br>
      3 - O aluno envia; <br>
      4 - O sistema armazena e entrega; <br>

          
          
