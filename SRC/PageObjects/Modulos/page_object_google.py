
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class page_object_google:
    def __init__(self, my_driver):
        self.driver = my_driver

    #Elementos del Form
        self.email = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        self.btn_siguiente = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        self.contraseña = (By.NAME, "Passwd")



    #Funcionalidad login

    def login(self, usr, pwd):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).send_keys(usr)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.btn_siguiente)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.contraseña)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.contraseña)).send_keys(pwd)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.btn_siguiente)).click()

    def btnsiguiente(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.btn_siguiente)).click()

