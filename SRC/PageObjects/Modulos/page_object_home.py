
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class page_object_home:
    def __init__(self, my_driver):
        self.driver = my_driver

    #Elementos del Form
        self.operador = (By.ID, ":R7almlm:")
        self.prestador = (By.ID, ":R9almlm:")



    #Funcionalidad login

    def click_operador(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.operador)).click()

    def click_prestador(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.prestador)).click()




    '''def switch_to_frame(self):

       self.driver.switch_to.frame(self.frame)

    '''
    def loginbutton(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.loginButton)).click()