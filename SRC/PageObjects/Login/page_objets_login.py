import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class page_object_login:
    def __init__(self, my_driver):
        self.driver = my_driver

    #Elementos del Form
        self.operador = (By.XPATH, "/html/body/div/div/div[2]/div/button[1]")
        self.prestador = (By.PARTIAL_LINK_TEXT, "Prestador")
        self.input_email = (By.XPATH,"//input[@type='email']")
        self.btn_next = (By.XPATH, "//span[text()='Siguiente']")
    #Funcionalidad login

    def click_operador(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.operador)).click()

    def click_prestador(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.prestador)).click()

    def click_input_email(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email)).send_keys(valor)

    def click_siguiente_email(self ):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_next)).click()




      #  WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ingreso_mail)).click()
       # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_mail)).send_keys(usr)
       # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_pass)).send_keys(pwd)
       # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.loginButton)).click()
   # def loginbutton(self):
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.loginButton)).click()