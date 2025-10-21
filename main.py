"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

try:
    # Configuración de Chrome para evitar el diálogo de contraseñas vulneradas
    options = Options()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Iniciar navegador con esas opciones
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificación
    assert '/inventory.html' in driver.current_url

    # Agregar producto al carrito
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()

    # Verificar carrito
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"
    print("TEST OK")

    time.sleep(10)

finally:
    driver.quit()
    """
    
    
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import shutil

tmp_profile = tempfile.mkdtemp(prefix="selenium-profile-")

try:
    options = Options()

    # 1) Prefs para desactivar el password manager y leak detection
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        # esta clave ayuda con el aviso de "contraseña vulnerada"
        "profile.password_manager_leak_detection": False
    })

    # 2) Flags para matar cualquier UI del password manager / leak detection
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,AutofillServerCommunication")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # 3) Perfil limpio para no heredar contraseñas guardadas ni sesiones
    options.add_argument(f"--user-data-dir={tmp_profile}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificación
    assert "/inventory.html" in driver.current_url

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"
    print("TEST OK")
    time.sleep(3)

finally:
    try:
        driver.quit()
    finally:
        shutil.rmtree(tmp_profile, ignore_errors=True)
