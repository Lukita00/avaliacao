from behave                 import given,when,then
from pages.cadastro_usuario import CadastroUsuario

cadastro = CadastroUsuario()

@given(u'que acesso a página de cadastro')
def step_impl(context):
    cadastro.abrir_cadastro()


@given(u'que preencho o formulário com nome = {nome}, email = {email} e senha = {senha}')
def step_impl(context,nome,email,senha):
    cadastro.preencher_cadastro(nome,email,senha)
    context.nome  = nome
    context.email = email


@when(u'clico no botão cadastrar')
def step_impl(context):
    cadastro.botao_cadastrar()

@then(u'visualizo os dados cadastrados')
def step_impl(context):
    cadastro.salva_tela(context.nome)
    assert(cadastro.get_resultado_nome,context.nome)
    assert(cadastro.get_resultado_email,context.email)

@then(u'visualizo o campo nome')
def step_impl(context):
    cadastro.salva_tela(context.nome)
    assert(cadastro.get_invalid_nome,'Por favor, insira um nome completo.')

@then(u'visualizo o campo email')
def step_impl(context):
    cadastro.salva_tela(context.nome)
    assert(cadastro.get_invalid_email,'Por favor, insira um e-mail válido.')

@then(u'visualizo o campo senha')
def step_impl(context):
    cadastro.salva_tela(context.nome)
    assert(cadastro.get_invalid_email,'A senha deve conter ao menos 8 caracteres.')
    