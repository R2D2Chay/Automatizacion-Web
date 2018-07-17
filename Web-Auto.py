#!/usr/local/bin/python
# coding: latin-1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestWebTituloPagina(unittest.TestCase):

    def setUp(self):
        # inicializa el webdriver
        self.driver = webdriver.Firefox()
        # agrega limpieza al salir
#        self.addCleanup(self.driver.quit)
#        browser = webdriver.Firefox()

#    def test_verificar_titulo_de_pagina(self):
#        # cambia la pagina web actual
#        self.driver.get('http://www.google.com')
#        # verifica que el primer texto se encuentre en otro
#        self.assertIn('Google', self.driver.title)
#        print "hola mundo" 

    def test_buscar_en_google(self):
        # cambia la pagina web actual
        self.driver.get('http://localhost:2012/pam-dashbuilder/')
        # identifica el campo de texto
        elemInputText = self.driver.find_element_by_name("j_username")
        # limpia el campo de texto
        elemInputText.clear()
        # agrega el texto
        elemInputText.send_keys("admin")
        # ingresa Password 
        elemInputText = self.driver.find_element_by_name("j_password")
        # limpia el campo de texto
        elemInputText.clear()
        # agrega el texto
        elemInputText.send_keys("$admin123")
        # presiona la tecla enter
        elemInputText.send_keys(Keys.RETURN)
        # espera 1 segundo
 #       self.driver.implicitly_wait(1)
        # verifica que el primer texto se encuentre en otro
 #       self.assertIn('zweicom', self.driver.current_url)

