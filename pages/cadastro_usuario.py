from pages.base_screen             import BaseScreen
from browser                       import Browser
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as ec

class Element(object):

    INPUT_NOME       = '//*[@id="name"]'
    INPUT_EMAIL      = '//*[@id="email"]'
    INPUT_SENHA      = '//*[@id="password"]'
    BUTTON_CADASTRAR = '//*[@id="register"]'

    PAGE_URL         = 'http://prova.stefanini-jgr.com.br/teste/qa/'

    RESULT_NOME      = '#tdUserName1'
    RESULT_EMAIL     = '#tdUserEmail1'

    INVALID_NOME     = '#root > div > div > div.register-form.expanded > form > div:nth-child(1) > p'
    INVALID_EMAIL    = '#root > div > div > div.register-form > form > div:nth-child(2) > p'
    INVALID_SENHA    = '#root > div > div > div.register-form > form > div:nth-child(3) > p'



class CadastroUsuario(BaseScreen,Browser):     
        
    def abrir_cadastro(self):
        self.acessar_pagina(Element.PAGE_URL)

    def preencher_cadastro(self,nome,email,senha):
        
        # preencher o nome de usuario
        self.preencher_campo(Element.INPUT_NOME,nome)
        # preencher o e-mail de usuario
        self.preencher_campo(Element.INPUT_EMAIL,email)
        # preencher a senha de usuario 
        self.preencher_campo(Element.INPUT_SENHA,senha)
            
    def botao_cadastrar(self):
        self.clicar_em(Element.BUTTON_CADASTRAR)

    def get_element(self,locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_resultado_nome(self):
        element = self.get_element(Element.RESULT_NOME)
        return element.text

    def get_resultado_email(self):
        element = self.get_element(Element.RESULT_EMAIL)
        return element.text

    def get_invalid_nome(self):
        element = self.get_element(Element.INVALID_NOME)
        return element.text

    def get_invalid_email(self):
        element = self.get_element(Element.INVALID_EMAIL)
        return element.text

    def get_invalid_senha(self):
        element = self.get_element(Element.INVALID_SENHA)
        return element.text


        