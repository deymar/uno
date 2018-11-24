from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^about/$', view=views.AboutView.as_view(), name='about'),
    url(regex=r'^bienvenida/$', view=views.BienvenidaView.as_view(), name='bienvenida'),
]