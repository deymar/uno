
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
        user_cuenta = UserProfile.objects.get(correo = "hoa@gmail.com")
        Debito.objects.create(monto='10.00', descripcion="prueba", user_cuenta=user_cuenta)
        Credito.objects.create(monto='10.00', descripcion="prueba", user_cuenta=user_cuenta)

        
        
    def test_credito(self):
        credit = Credito.objects.get(descripcion="prueba")
        self.assertNotEqual(credit.monto, '0.00')

    def test_user(self):
        usuario = User.objects.get(username = "prueba")
        self.assertEqual(usuario.password, "1234")

    def test_servicio(self):
        pago = PagoServicio.objects.get(cuenta_servicio = "cuenta")
        self.assertNotEqual(pago.monto, '0.00')
        self.assertEqual(pago.user_cuenta, "prueba")

    def test_transferencia(self):
        transfer = Transferencia.objects.get(user_cuenta = "usuario1")
        self.assertIsNotNone(transfer.user_cuenta2)
