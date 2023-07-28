import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://dosmartqa.stagsoftware.net:3009/login')
time.sleep(3)

driver.find_element(By.XPATH,"//input[@class='form-input-feild ng-untouched ng-pristine ng-invalid']").send_keys('sridhar_ramesh')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('Golu@1997')
time.sleep(3)
driver.find_element(By.XPATH,"//button[@id='login-form-submit']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@id='projectselectExistOpen']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@data-toggle='modal']").click()
time.sleep(3)
