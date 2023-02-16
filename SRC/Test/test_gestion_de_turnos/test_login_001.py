''' credenciales
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

from SRC.PageObjects.Login.page_objets_login import page_object_login
from SRC.PageObjects.Modulos.page_object_google import page_object_google
from SRC.PageObjects.Modulos.page_object_home import page_object_home
from SRC.PageObjects.Modulos.page_object_operador import page_object_operador
from SRC.PageObjects.Modulos.page_object_nuevo_turno import page_object_nuevo_turno
from selenium.webdriver.common.alert import Alert
from random import randint
# Importaciones Modulos
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import unittest
import json
import time


class TC_traditum_login_google(unittest.TestCase):

    def setUp(self):
        # Carga de JSONS

        with open(r"D:/AUTOMATION TRADITUM/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"D:/AUTOMATION TRADITUM/SRC/datos/Config.Json") as ambiente2:
            self.ambiente_traditum = json.loads(ambiente2.read())

        with open(r"D:/AUTOMATION TRADITUM/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"D:/AUTOMATION TRADITUM/SRC/datos/User.Json") as usuario:
            self.diccionario_usuario = json.loads(usuario.read())

        with open(r"D:/AUTOMATION TRADITUM/SRC/datos/Nombres.Json") as nombres:
            self.diccionario_nombres = json.loads(nombres.read())

        # Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        time.sleep(10)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_webtest["ambiente"][0])

        # Config de Pages

        self.login = page_object_login(self.driver)
        self.logingoogle = page_object_google(self.driver)
        self.traditum = page_object_home(self.driver)
        self.operador= page_object_operador(self.driver)
        self.nuevo_turno = page_object_nuevo_turno(self.driver)
        # Usuario contraseña

        usr = self.diccionario_usuario["UserAsistente"][0]
        pwd = self.diccionario_usuario["PassAsistente"][0]
        self.logingoogle.login(usr, pwd)
        # self.login.loginButton()
        #self.assertNotEqual(("https://webtest.medife.com.ar/portal/mis-gestiones"), None)

    def test_login_traditum(self):

        time.sleep(10)
        self.driver.get("https://camdoctor-telemedicina-qa.web.app/")
        self.traditum.click_operador()
        time.sleep(10)
        self.operador.click_gestion_de_turno()
        self.operador.click_nuevo_turno()
        time.sleep(10)
        self.operador.click_financiador()
        self.operador.click_swiss()
        self.operador.click_btn_siguiente()
        time.sleep(5)
        EC.visibility_of_element_located((By.XPATH, "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/div[2]/div[2]"))
        self.nuevo_turno.click_cuil_asociado()
       # self.nuevo_turno.insertar_cuit(20376472079)
        time.sleep(5)
        #self.nuevo_turno.click_motivo_de_consulta()
        #self.nuevo_turno.click_consulta_inicial()
        #self.operador.click_btn_siguiente()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Complete")


if __name__ == "__main__":
    unittest.main()
