# tests/test_carrito.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto(login_in_driver):
    try:
        driver = login_in_driver
        #Espera para que cargue elementos
        wait = WebDriverWait(driver, 20)
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert items, "No se encontraron productos en el inventario"
        first = items[0]
        first_name = first.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert first_name, "El primer producto no tiene nombre visible"
        first.find_element(By.TAG_NAME, "button").click()
        badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert badge.text == "1", f"Se esperaba '1', fue '{badge.text}'"
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("/cart.html"))
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert cart_items, "No hay items en el carrito"
        cart_names = [ci.find_element(By.CLASS_NAME, "inventory_item_name").text for ci in cart_items]
        assert first_name in cart_names, f"'{first_name}' no aparece en el carrito: {cart_names}"
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
