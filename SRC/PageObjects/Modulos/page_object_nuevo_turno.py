from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
import random

class page_object_nuevo_turno:

    def __init__(self, my_driver):
        self.driver = my_driver


        self.cuilAsociado = (By.CSS_SELECTOR,  "div.MuiBox-root.css-0 div.MuiBox-root.css-ogmp5q main.css-104qyot div.MuiBox-root.css-0 div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiCard-root.css-fn6sn0 div.MuiCardContent-root.css-18mhetb div.slick-slider.jss15.slick-initialized div.slick-list div.slick-track div.slick-slide.slick-active.slick-current:nth-child(2) div:nth-child(1) div.MuiBox-root.css-1yfbaa6 div.jss20.MuiBox-root.css-0:nth-child(1) div.MuiFormControl-root.MuiTextField-root.css-i44wyl:nth-child(1) > div.MuiInput-root.MuiInput-underline.MuiInputBase-root.MuiInputBase-colorPrimary.MuiInputBase-formControl.MuiInputBase-adornedEnd.css-1oan4od")
        self.insertar_cuit = (By.XPATH, "//label[@id=':r7:-label']")
        self.btn_atras = (By.XPATH, "//body/div[@id='__next']/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/button[1]")
        self.motivo_de_consulta = (By.CSS_SELECTOR,"div.MuiBox-root.css-0 div.MuiBox-root.css-ogmp5q main.css-104qyot div.MuiBox-root.css-0 div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiCard-root.css-fn6sn0 div.MuiCardContent-root.css-18mhetb div.slick-slider.jss15.slick-initialized div.slick-list div.slick-track div.slick-slide.slick-active.slick-current:nth-child(2) div.MuiBox-root.css-1yfbaa6 div.jss20.MuiBox-root.css-0:nth-child(3) div.MuiFormControl-root.MuiFormControl-fullWidth.css-tzsjye:nth-child(3) div.MuiInput-root.MuiInput-underline.MuiInputBase-root.MuiInputBase-colorPrimary.MuiInputBase-formControl.css-4cj459 > div.MuiSelect-select.MuiSelect-standard.MuiInput-input.MuiInputBase-input.css-qzsybu")
        self.consulta_inicial =(By.CSS_SELECTOR ,"body:nth-child(2) div.MuiModal-root.MuiPopover-root.MuiMenu-root.css-1sucic7:nth-child(32) div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation0.MuiMenu-paper.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation8.MuiPopover-paper.css-6s1i02:nth-child(3) ul.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 > li.MuiMenuItem-root.MuiMenuItem-gutters.MuiButtonBase-root.css-a4ygnu:nth-child(2)")

    def click_cuil_asociado(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuilAsociado)).click()

    def insertar_cuit_asosciado(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.insertar_cuit)).send_keys(valor)

    def click_motivo_de_consulta(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.motivo_de_consulta)).click()

    def click_consulta_inicial(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.consulta_inicial)).click()

    def click_btn_atras(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_atras)).click()

