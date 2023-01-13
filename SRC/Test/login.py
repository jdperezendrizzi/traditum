import sys
import HtmlTestRunner

sys.path.append(r"/\\")

from SRC.PageObjects.Login.page_objets_login import PageObjectLogin
from selenium.webdriver.common.alert import Alert
from random import randint
from selenium import webdriver
import unittest
import json
import time

sys.path.append(r"/Infinitus\\")

# Importaciones de Page

#from utils.oracle_driver_operation s import ConsultaBaseDatos

# Importaciones Modulos
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import json

class CTlogin001(unittest.TestCase):

    def setUp(self):

        with open(r"D:/Automationprueba/SRC/datos/Config.Json") as ambiente:
            self.ambiente_issuerLINK = json.loads(ambiente.read())

        with open(r"D:/Automationprueba/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"D:/Automationprueba/SRC/datos/User.Json") as usuario:
            self.diccionario_usuario = json.loads(usuario.read())

        with open(r"D:/Automationprueba/SRC/datos/Nombres.Json") as nombres:
            self.diccionario_nombres = json.loads(nombres.read())

# Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_issuerLINK["ambiente"][0])

# Config de Pages

        self.login = PageObjectLogin(self.driver)

# Usuario contraseña


        usr = self.diccionario_usuario["User"][0]
        pwd = self.diccionario_usuario["Pass"][0]
        self.login.login(usr, pwd)
        self.assertNotEqual(("https://webtest.medife.com.ar/"), None)

#test

    def test_login_001(self):



        # assert
        '''validacion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/div/div/div[1]/div/div[3]/div[2]/form/div[2]/p"))).is_displayed()
        self.assertEqual(validacion, True)'''


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()