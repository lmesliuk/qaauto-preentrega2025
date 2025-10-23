from selenium.webdriver.common.by import By
from selenium import webdriver

def test_validacion_login(login_in_driver):
    try:
        driver = login_in_driver
        #Verificación de la página de inventario
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise






