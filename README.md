# Projeto Back-End 

Grupo:

Henrique Cals, Guilherme Pinon, Caio Cunha, Henrique Mundy, João Pedro Sampaio e Pedro Paulo

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
    ####Contas
      RF01 -> O sistema deve permitir a criação de contas de usuário. <br>
      RF02 -> O sistema deve validar os dados informados no cadastro. <br>
      RF03 -> O sistema deve criptografar dados sensíveis do usuário. <br>
      RF04 -> O sistema deve enviar e-mail de verificação com link de confirmação. <br>
      RF05 -> O sistema deve permitir login no sistema. <br>
      RF06 -> O sistema deve permitir alteração dos dados da conta. <br>
      RF07 -> O sistema deve permitir recuperação de senha. <br>
      RF08 -> O sistema deve realizar exclusão lógica de contas. <br>
      RF09 -> O sistema deve permitir visualização dos dados da conta. <br>





 # Casos de Uso de forma narrativa

## Caso de Uso 1 - Cadastro em Estágio
* Ator - Aluno  <br>
  * Descrição - Aluno cadastrar as informações do estágio no sistema.  <br>

    * Fluxo principal: <br>
      1 - O aluno acessa o sistema; <br>
      2 - O aluno cria uma conta; <br>
      3 - O aluno realiza login; <br>
      4 - O aluno seleciona a opção de cadastrar estágio; <br>
      5 - O aluno preenche os campos das informações; <br>
      6 - O aluno confirma o cadastro; <br>
      7 - O sistema valida os dados; <br>
      8 - O sistema registra o estágio. <br>

        * Fluxo Alternativo: <br>
           --> 4.1) O aluno informa dados inválidos ou incompletos <br>  |-- Gera erro e solicitação de correção do sistema; <br>
           --> 7.1) O sistema já possui esse estágio cadastrado <br>  |-- Gera erro e impede a duplicação.<br>

## Caso de Uso 2 - Envio de Relatório
* Ator - Aluno  <br>
  * Descrição - Aluno enviar relatórios sobre o estágio.  <br>

    * Fluxo principal: <br>
      1 - O aluno acessa o sistema; <br>
      2 - O aluno cria uma conta; <br>
      3 - O aluno realiza login; <br>
      4 - O aluno seleciona a opção de cadastrar estágio; <br>
      5 - O aluno preenche os campos das informações; <br>
      6 - O aluno confirma o cadastro; <br>
      7 - O sistema valida os dados; <br>
      8 - O sistema registra o estágio. <br>

        * Fluxo Alternativo: <br>
           --> 4.1) O aluno informa dados inválidos ou incompletos <br>  |-- Gera erro e solicitação de correção do sistema; <br>
           --> 7.1) O sistema já possui esse estágio cadastrado <br>  |-- Gera erro e impede a duplicação.<br>
