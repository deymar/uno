from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
import uuid

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nombre = models.CharField(max_length=50, null=False)
    correo = models.EmailField(unique=True, null=False)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    def __str__(self):
        return str(self.codigo)
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

class Servicio(models.Model):
    servicio = models.CharField(primary_key=True, max_length=30, null=False)
    def __str__(self):
        return self.servicio
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

class Transferencia(models.Model):
    user_cuenta = models.CharField(max_length=60, null=False)
    user_cuenta2 = models.CharField(max_length=60, null=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    def __str__(self):
        return str(self.monto)
    class Meta:
        verbose_name = 'Transferencia'
        verbose_name_plural = 'Transferencias'

class Credito(models.Model):
    user_cuenta = models.ForeignKey(UserProfile, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    descripcion = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Credito'
        verbose_name_plural = 'Creditos'

class Debito(models.Model):
    user_cuenta = models.ForeignKey(UserProfile, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    descripcion = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Debito'
        verbose_name_plural = 'Debitos'

class PagoServicio(models.Model):
    cuenta_servicio = models.CharField(max_length=50, null=False)
    tipo_servicio = models.CharField(max_length=100, null=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    user_cuenta = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.tipo_servicio)
    class Meta:
        verbose_name = 'Pago de Servicio'
        verbose_name_plural = 'Pago de Servicios'