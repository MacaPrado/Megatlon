from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Megatlon:

    def __init__(self, user_mail, password):
        self.user_mail = user_mail
        self.password = password

    def reserve_class(self, location, day, class_name, timing):
        location = location
        day = day
        class_name = class_name
        timing = timing

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://megatlon.com/')

        time.sleep(1)

        # Log In
        Login = driver.find_element_by_xpath('//*[@id="menu"]/li[9]/a')
        Login.click()

        # User Mail
        user = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[1]/label/input')
        user.send_keys(self.user_mail)

        # Pass
        password = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[2]/label/input')
        password.send_keys(self.password)

        submit = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[4]/button')
        submit.click()

        time.sleep(3)

        new_class = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a')
        new_class.click()

        time.sleep(1)

        # Selecciono la sede a la que quiero ir
        wait = WebDriverWait(driver, 15)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div[2]/div').click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[contains(text(),"' + location + '")]'))).click()

        # Busco la clase que me interesa asistir
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH,
             '//div[contains(h6[1],"' + day + '") and contains(h5,"' + class_name + '") and contains(h6[2],"' + timing + '")]'))).click()

        # Reservo
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//button[text()="Reservar"]'))).click()

        time.sleep(3)

        driver.close()
