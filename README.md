# **📌 Python Selenium Behave - Framework de Automatización de Pruebas**

![Selenium + Behave](https://img.shields.io/badge/Selenium-Behave-green) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen)

## **🔹 Descripción**
Este proyecto utiliza **Python, Selenium y Behave** para la automatización de pruebas **end-to-end** en aplicaciones web. Implementa el **Modelo de Objetos de Página (POM)** para mejorar la mantenibilidad y la legibilidad del código.

---

## **📁 Estructura del Proyecto**
```bash
/project
  ├── /features
  │    ├── /steps
  │    │    ├── login_steps.py
  │    ├── /pages
  │    │    ├── base_page.py
  │    │    ├── login_page.py
  │    ├── login.feature
  ├── /utils
  │    ├── config.py
  │    ├── driver_factory.py
  ├── environment.py
  ├── requirements.txt
  ├── README.md
```

---

## **🚀 Instalación y Configuración**

## **🛠 Instalación de Dependencias**
Para ejecutar este proyecto, es necesario instalar las siguientes dependencias en un entorno de **Python 3.8+**.

### **1️⃣ Instalar Virtual Environment (Opcional pero recomendado)**
Antes de instalar las dependencias, se recomienda crear un entorno virtual para aislar las librerías.

```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate    # En Windows
```

### **2️⃣ Instalar las Dependencias**
Ejecuta el siguiente comando para instalar todas las dependencias necesarias desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

### **3️⃣ Instalar Selenium WebDriver**
Para ejecutar pruebas con Selenium, debes descargar y agregar el controlador correspondiente a tu navegador:

- **ChromeDriver:** [Descargar ChromeDriver](https://chromedriver.chromium.org/downloads)
- **GeckoDriver (Firefox):** [Descargar GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- **Edge WebDriver:** [Descargar EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Una vez descargado, agrégalo a la variable de entorno **PATH**.

---

## **📜 Archivo de Dependencias (`requirements.txt`)**
Si necesitas generar el archivo `requirements.txt`, usa:

```bash
pip freeze > requirements.txt
```

Ejemplo de un `requirements.txt`:
```txt
behave
selenium
pytest
requests
```

---

## **🔹 Extensiones Recomendadas para VS Code**
Si utilizas **Visual Studio Code**, se recomienda instalar las siguientes extensiones:

1. **Python** - Soporte para desarrollo en Python.
2. **Pylance** - Análisis de código y autocompletado.
3. **Behave VSC** - Soporte para Gherkin y Behave.
4. **Test Explorer UI** - Para visualizar y ejecutar pruebas de Behave.
5. **Debugger for Chrome** - Para depurar pruebas en navegadores.

Puedes instalarlas desde la **Marketplace de VS Code** o ejecutar:

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension talonmies.behave-vsc
code --install-extension hbenl.test-explorer
code --install-extension msjsdiag.debugger-for-chrome
```

---

## **📌 Verificación de Instalación**
Para comprobar que todo está correctamente instalado, ejecuta:

```bash
python --version
pip list
behave --version
```

Si todo está bien, puedes comenzar a ejecutar tus pruebas con `behave`. 🚀

---

## **📝 Creación de Escenarios de Prueba**
Los escenarios **Gherkin** se escriben dentro de la carpeta `/features/`.

Ejemplo (`features/login.feature`):
```gherkin

Feature: Logging
Scenario: Successful logging
    Given the user is on the login page
    When the user enters "prueba12@gmail.com" as username
    And the user enters "*Prueba123" as password
    And the user clicks the login button
    Then the user should be redirected to the dashboard
```

---

## **⚡ Ejecutar Pruebas**
### **Ejecutar todas las pruebas**
```bash
behave
```

### **Ejecutar una funcionalidad específica**
```bash
behave features/login.feature
```

```bash
behave features/signup.feature
```

### **Ejecutar un escenario específico por etiqueta**
```bash
behave --tags=@smoke
```

### **Ejecutar un escenario específico por número de línea**
```bash
behave features/login.feature:5

```
### **Ejecutar con reporte html**

- primero descargar la dependencia:
```bash
pip install behave selenium behave-html-formatter

```

- luego ejecutar el siguiente comando en cmd:
```bash
behave -f html -o reports/behave-report.html


```

---


## **📜 Ejemplo de POM (Page Object Model)**
Ejemplo de `features/pages/login_page.py`:

```python
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")

    def enter_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
```

---

## **📝 Autor y Contribuciones**
- **👨‍💻 Daniel David Cardona**
- Repositorio creado para prueba qa automatizador
- link resporte de bugs: https://www.notion.so/Seguimiento-de-bugs-inlaze-1a6baf1db86d806794b7d012ee8938ad?pvs=4
- link casos de prueba: https://www.notion.so/Reto-automatizaci-n-inlaze-ebf81068e30146f3bb5317dd9460bd02?pvs=4
- video resumen proyecto: https://youtu.be/SVgGKlJbvI8

## **📝 Notas Adicionales**
- debido al corto tiempo el proyecto requiere de refactorización

