from selenium import webdriver
import time

class Whatsapp_bot:
    def __init__(self):
        self.mensagem = "Bom dia galerinha"
        self.grupos = ["Grupo1", "Grupo2"] #O nome tem que ser idêntico
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def comentarios(self):
        #html do grupo = a
        #html do chat = b
        #html do botao de envio = c

        self.driver.get('site')
        for grupo in self.grupos:
            grupo = self.driver.find_elements_by_xpath(f"//spam[@title='{grupo}']") #a
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_elements_by_class_name('_13mgZ') #b
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_elements_by_xpath("//spam[@data_icon='send']") #c
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

        return