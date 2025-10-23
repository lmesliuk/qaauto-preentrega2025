import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import login
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()

    # 🔹 Evita el cartel de "contraseña vulnerada" y el password manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    opts.add_experimental_option("prefs", prefs)

    # 🔹 Oculta el mensaje "Chrome is being controlled by automated test software"
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)

    # ✅ Desactiva explícitamente la detección de contraseñas filtradas
    opts.add_argument("--disable-features=PasswordLeakDetection")
    opts.add_argument("--disable-features=PasswordManagerOnboarding")
    drv = webdriver.Chrome(options=opts)
    drv.maximize_window()
    yield drv
    drv.quit()
    
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver

@pytest.fixture
def carrito_un_item(login_in_driver):
    driver = login_in_driver
    # Agregar primer producto
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    return driver