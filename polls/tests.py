from django.test import TestCase
from django.contrib.auth.models import User
from selenium import webdriver  # Importar Selenium WebDriver
from selenium.webdriver.chrome.options import Options  # Importar Options para configurar el navegador

class PollsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Configurar las opciones del navegador (en este caso, Chrome)
        opts = Options()
        opts.add_argument("--headless")  # Ejecutar en modo sin cabeza (sin interfaz gráfica)
        opts.add_argument("--disable-gpu")  # Deshabilitar GPU para evitar errores
        opts.add_argument("--no-sandbox")  # Necesario en algunos entornos

        # Inicializar el WebDriver de Selenium con las opciones configuradas
        cls.selenium = webdriver.Chrome(options=opts)
        cls.selenium.implicitly_wait(5)  # Esperar hasta 5 segundos para encontrar elementos

        # Crear un superusuario para las pruebas
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()

    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar las pruebas
        cls.selenium.quit()
        super().tearDownClass()

    def test_superuser_exists(self):
        # Comprobar que el superusuario se ha creado correctamente
        self.assertTrue(User.objects.filter(username="isard").exists())
