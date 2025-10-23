from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, user="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)  # subí a 20s por las dudas

    # Esperar inputs visibles antes de escribir
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Esperar la redirección al inventario
    wait.until(EC.url_contains("/inventory.html"))