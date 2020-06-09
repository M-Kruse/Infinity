#!/usr/bin/env python3
import os
import time
import random
import string
from shutil import which

import names

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

assert which("geckodriver"), "ERROR: Could not locate geckodriver in $PATH"
assert which('macchanger'), "ERROR: Could not locate macchanger in $PATH"

class User(object):
    """docstring for User"""
    def __init__(self):
        super(User, self).__init__()
        self.domains = [
            "hotmail.com",
            "gmail.com",
            "aol.com",
            "mail.com",
            "mail.kz",
            "yahoo.com"
        ]
        self.seperators = ["-", ".", "", "_"]
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.email = "{0}{1}{2}{3}@{4}".format(
            self.first_name,
            self.seperators[random.randrange(0, len(self.seperators))],
            self.last_name,
            ''.join(random.choice(string.digits) for _ in range(random.randrange(1, 5))),
            self.domains[random.randrange(0, len(self.domains))]
        )
        self.secret_answer = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        self.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(24))

class Infinity(object):
    """docstring for Infinity"""
    def __init__(self, wlan_inf):
        super(Infinity, self).__init__()
        self.wlan_inf = wlan_inf
        self.max_delay = 20
        self.driver = webdriver.Firefox()

    def is_internet_accessible(self):
        r = os.system("ping -W 5 -c 1 8.8.8.8 >/dev/null 2>&1")
        return bool(r == 0)

    def set_wifi_state(self, enabled=True):
        if enabled == True:
            state = "on"
        else:
            state = "off"
        os.system("nmcli radio wifi {}".format(state))

    def randomize_mac(self):
        os.system("sudo macchanger -r {0}".format(self.wlan_inf))

    def connect_wifi(self):
        os.system("nmcli device wifi connect xfinitywifi")

    def random_sleep(self, min_sleep=1, max_sleep=2):
        time.sleep(random.randrange(min_sleep, max_sleep))

    def handle_portal(self, user):
        self.driver.get("http://detectportal.firefox.com/success.txt")
        WebDriverWait(self.driver, self.max_delay).until(EC.presence_of_element_located((By.ID, 'banner_green_text')))
        self.driver.get(self.driver.find_element_by_id("banner_green_text").get_attribute("href"))
        WebDriverWait(self.driver, self.max_delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'small-10')))
        self.driver.find_element_by_class_name("small-10").click()
        self.random_sleep()
        self.driver.find_element_by_id("continueButton").click()
        self.random_sleep()
        self.driver.find_element_by_id("upgradeOfferCancelButton").click()
        WebDriverWait(self.driver, self.max_delay).until(EC.presence_of_element_located((By.ID, 'firstName')))
        self.driver.find_element_by_id("firstName").send_keys(user.first_name)
        self.driver.find_element_by_id("lastName").send_keys(user.last_name)
        self.random_sleep()
        self.driver.find_element_by_id("usePersonalEmail").click()
        WebDriverWait(self.driver, self.max_delay).until(EC.presence_of_element_located((By.ID, 'primaryEmail')))
        self.random_sleep()
        self.driver.find_element_by_id("primaryEmail").send_keys(user.email)
        self.driver.find_element_by_id("dk0-combobox").click()
        self.driver.find_elements_by_class_name("dk-option")[random.randrange(1, 4)].click()
        self.random_sleep()
        self.driver.find_element_by_id("secretAnswer").send_keys(user.secret_answer)
        self.random_sleep()
        self.driver.find_element_by_id("password").send_keys(user.password)
        self.random_sleep()
        self.driver.find_element_by_id("passwordRetype").send_keys(user.password)
        self.random_sleep()
        self.driver.find_element_by_id("submitButton").click()
        WebDriverWait(self.driver, self.max_delay).until(EC.presence_of_element_located((By.ID, '_orderConfirmationActivatePass')))
        time.sleep(1) # replace with a wait for div class spinner-on to go missing
        self.driver.find_element_by_id("_orderConfirmationActivatePass").click()