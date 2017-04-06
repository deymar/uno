
from django.contrib.auth.models import User
from django.test import TestCase

from sistema.models import Credito, Debito, PagoServicio, Servicio, UserProfile, Transferencia


class ServicioTest(TestCase):
    def setUp(self):
        User.objects.create(password="1234", username="prueba", email="prueba@gmail.com")
        usuario = User.objects.get(username = "prueba")
        Transferencia.objects.create(user_cuenta = "usuario1", user_cuenta2 = "usuario2", monto = '25.00')
        UserProfile.objects.create(correo="hoa@gmail.com", nombre="hola", user = usuario)
        Servicio.objects.create(servicio="luz")
        Servicio.objects.create(servicio="cable")
        cable = Servicio.objects.get(servicio = "cable")
        PagoServicio.objects.create(cuenta_servicio="cuenta", tipo_servicio = cable, user_cuenta = "prueba", monto='10.00')        
        user_cuenta = UserProfile.objects.get(correo = "hola@gmail.com")
        Debito.objects.create(monto='10.00', descripcion="prueba", user_cuenta=user_cuenta)
        Credito.objects.create(monto='10.00', descripcion="prueba", user_cuenta="user_cuenta")
        
   
    def test_user(self):
        user = User.objects.get(username = "prueba")
        self.assertNotNull(user.username)

        
    def test_credito(self):
        credit = Credito.objects.get(descripcion="prueba")
        self.assertNotEqual(credit.monto, '0.00')

