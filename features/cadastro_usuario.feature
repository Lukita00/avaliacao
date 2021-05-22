#language:pt

Funcionalidade: Realizar cadastro de usuário

Contexto: Acessar a página de teste
Dado que acesso a página de cadastro

Cenário: Realizar cadastro
Dado que preencho o formulário com nome = lucas araujo, email = lucas@teste.com.br e senha = 12345678
Quando clico no botão cadastrar
Então visualizo os dados cadastrados

Cenário: Realizar cadastro com nome inválido
Dado que preencho o formulário com nome = sarah, email = sarah@teste.com.br e senha = 1020304050
Quando clico no botão cadastrar
Então visualizo o campo nome

Cenário: Realizar cadastro com email inválido
Dado que preencho o formulário com nome = Mateus Azevedo, email = mateus.com.br e senha = biscoito
Quando clico no botão cadastrar
Então visualizo o campo email

Cenário: Realizar cadastro com senha inválida
Dado que preencho o formulário com nome = João Carlos, email = joao@teste.com e senha = 1234
Quando clico no botão cadastrar
Então visualizo o campo senha