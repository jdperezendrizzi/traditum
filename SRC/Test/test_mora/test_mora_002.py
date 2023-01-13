''' Cuenta Sin MORA
TC
'''
import inspect
import sys
import time
from random import randint, random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import HtmlTestRunner
import sys
import time
from random import randint, random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.color import Color
import HtmlTestRunner

sys.path.append(r"/\\")

# Importaciones de Page

from SRC.PageObjects.Login.page_objets_login import PageObjectLogin
from SRC.PageObjects.Modulos.page_object_credenciales import page_object_credenciales
from selenium.webdriver.common.alert import Alert
from random import randint
# Importaciones Modulos

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest
import json
import time


class TCcedenciales001(unittest.TestCase):

    def setUp(self):
        # Carga de JSONS

        with open(r"D:/AUTOMATION WEB MEDIFE/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"D:/AUTOMATION WEB MEDIFE/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"D:/AUTOMATION WEB MEDIFE/SRC/datos/User.Json") as usuario:
            self.diccionario_usuario = json.loads(usuario.read())

        with open(r"D:/AUTOMATION WEB MEDIFE/SRC/datos/Nombres.Json") as nombres:
            self.diccionario_nombres = json.loads(nombres.read())

        # Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_webtest["ambiente"][0])

        # Config de Pages

        self.login = PageObjectLogin(self.driver)
        self.page_object_credenciales = page_object_credenciales(self.driver)

        # Usuario contraseña

        usr = self.diccionario_usuario["User"][0]
        pwd = self.diccionario_usuario["Pass"][0]
        self.login.login(usr, pwd)
        # self.login.loginButton()
        #self.assertNotEqual(("https://webtest.medife.com.ar/portal/mis-gestiones"), None)

    def test_credenciales_001(self):

        time.sleep(20)
       # self.page_object_credenciales.click_fondo_home()
        time.sleep(8)

        #self.page_object_credenciales.click_detalle_credencial()
        self.assertEqual(self.driver.find_element(By.XPATH, "/html/body/app-root/app-header/div[3]/div/div/div[1]/nav/ol/li/a").text, 'Mi Cuenta')




    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
