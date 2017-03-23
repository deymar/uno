from django.contrib import admin

from .models import UserProfile, Servicio, PagoServicio, Credito, Debito, Transferencia

admin.site.register(UserProfile)
admin.site.register(Servicio)
admin.site.register(PagoServicio)
admin.site.register(Credito)
admin.site.register(Debito)
admin.site.register(Transferencia)

# Register your models here.
