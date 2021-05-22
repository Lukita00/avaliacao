from selenium                      import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BaseScreen:

    # metodo para acessar pagina da web
    def acessar_pagina(self,url):

        self.driver.get(url)

    # metodo para preencher um campo mapeado com o texto informado
    def preencher_campo(self,xpath,texto):

        self.driver.find_element_by_xpath(xpath).send_keys(texto)

    # metodo que clica em um elemento da mapeado
    def clicar_em(self,xpath):

        self.driver.find_element_by_xpath(xpath).click()

    # metodo que salva um screenshot da tela
    def salva_tela(self,nome):

        self.driver.save_screenshot(fr'screenshot/{nome}.png')