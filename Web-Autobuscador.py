#!/usr/local/bin/python
# coding: latin-1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time 

driver = webdriver.Firefox()
driver.get('http://www.autobuscador.cl/')


