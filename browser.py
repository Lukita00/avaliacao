from selenium import webdriver

class Browser(object):
    # inicia o browser
    driver = webdriver.Edge()
    # timeout da pagina
    driver.set_page_load_timeout(30)
    # maximiza o tela
    driver.maximize_window()


    # fecha o navegador
    def browser_quit(self):
        self.driver.quit()
    

    # limpa o navegador
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()
        