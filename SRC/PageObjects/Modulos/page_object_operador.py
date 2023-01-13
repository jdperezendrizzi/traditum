from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
import random

class page_object_operador:

    def __init__(self, my_driver):
        self.driver = my_driver

        self.gestion_de_turno = (By.XPATH, "//*[@id='__next']/div/div/main/div/div[1]/div[1]/li/div[1]/div[2]/p")
        self.nuevo_turno = (By.XPATH, "//*[@id='__next']/div/div/main/div/div[1]/div[2]/div/div[1]/button/div/div[2]/p")
        self.financiadorlista = (By.ID, "mui-component-select-financiador")
        self.swiss_medical_asistente1 =(By.XPATH ,"//*[@id='menu-financiador']/div[3]/ul/li[1]")
        self.btn_siguiente =(By.XPATH,"//*[@id='__next']/div/div/main/div/div[1]/div[2]/div[3]/div/button")

    def click_gestion_de_turno(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.gestion_de_turno)).click()

    def click_nuevo_turno(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nuevo_turno)).click()

    def click_financiador(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.financiadorlista)).click()

    def click_swiss(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.swiss_medical_asistente1)).click()





    def select_financiador(self, valor):
        select_element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.financiadorlista))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def click_btn_siguiente(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_siguiente)).click()

    def click_random(self):
    def click_foto_credencial(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.foto_credencial)).click()

    def click_ayuda(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ayuda)).click()

    def click_fondo_home(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.fondo_home)).click()



    def select_emisor_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.emisor_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_marca_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.marca_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_producto_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.producto_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_sucursal_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sucursal_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_grupo_afinidad(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.grupo_afinidad))
        select_object = Select(select_element)
        select_object.select_by_index(valor)



  #NACIONALIDAD
    def select_nacionalidad (self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.nacionalidad))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_tipoDocu(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.tipoDocu))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def ingresar_documento(self, random):
        random = randint(10000000, 99999999)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.documento)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.documento)).send_keys(random)

    def ingresar_apellido(self, apellido):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apellido)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apellido)).send_keys(str(apellido))

    def ingresar_nombre(self, nombre):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre)).send_keys(str(nombre))

    def ingresar_cuit_cuil(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuit_cuil)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuit_cuil)).send_keys(valor)



    def select_sexo(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sexo))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def ingresar_fecha_nacimiento(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.fecha_nacimiento)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.fecha_nacimiento)).send_keys(valor)



    def ingresar_cuenta_ext(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuenta_ext)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuenta_ext)).send_keys(valor)

    def ingresar_email(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).send_keys(valor)

    def select_pais (self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.pais))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_depto_prov (self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.depto_prov))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def ingresar_localidad(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.localidad)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.localidad)).send_keys(valor)

    def ingresar_calle(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.calle)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.calle)).send_keys(valor)

    def ingresar_numero(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.numero)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.numero)).send_keys(valor)

    def ingresar_CD(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.codigo_postal)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.codigo_postal)).send_keys(valor)

    def ingresar_telefono(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.telefono)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.telefono)).send_keys(valor)


    def ingresar_nombre_embozado(self,valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre_embozado)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre_embozado)).send_keys(valor)

    def grabar_alta(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.grabar)).click()

    def confirmar_aceptar_prenovedad(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.aceptar_prenovedad)).click()


