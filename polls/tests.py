from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User

class PollsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
        # creem superusuari
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()


    def tearDownClass(cls):
        # tanquem browser
        # comentar la propera línia si volem veure el resultat de l'execució al navegador
        cls.selenium.quit()
        super().tearDownClass()

    def test_superuser_exists(self):
        # Comprobar que el superusuario se ha creado correctamente
        self.assertTrue(User.objects.filter(username="isard").exists())
