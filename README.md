# qaauto-preentrega2025
Pre-entrega TP QA Automation 2025

------------------------
Propósito del proyecto:
Automatizar los siguientes flujos en la página  SauceDemo
1) Login con credenciales válidas e inválidas
2) Verificación del catálogo de productos
3) Interacción con el carrito de compras (añadir productos y verificar su contenido)
4) Cierre de sesión
------------------------
Tecnologías utilizadas:
1) Python: Lenguaje de programación principal
2) Pytest: Framework de testing para estructurar y ejecutar pruebas
3) Selenium WebDriver: Para la automatización de la interfaz web
4) Git/GitHub: Para control de versiones y compartir el código
------------------------
Estructura del proyecto

qaauto-preentrega2025/
│
├── conftest.py # Configuración Pytest
├── README.md # Explicación
├── utils.py # Funciones auxiliares
├── runtests.py # Ejecución de tests y reporte
├── tests/ # Carpeta con los tests
│ ├── test_login.py
│ ├── test_inventory.py
│ └── test_carrito.py
└── reporte.html #Reporte

------------------------
Dependencias
pip install selenium
pip install pytest
------------------------

Pautas:
------------------------
Automatización de Login:
------------------------
Navegar a la página de login de saucedemo.com

Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")

Validar login exitoso verificando que se haya redirigido a la página de inventario
------------------------
Navegación y Verificación del Catálogo: (Clases 6 a 8)

Caso de Prueba de Navegación:

Verificar que el título de la página de inventario sea correcto

Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
------------------------
Interacción con Productos: (Clase 8)

Caso de Prueba de Carrito:

Añadir un producto al carrito haciendo clic en el botón correspondiente

Verificar que el contador del carrito se incremente correctamente

Navegar al carrito de compras

Comprobar que el producto añadido aparezca correctamente en el carrito
------------------------