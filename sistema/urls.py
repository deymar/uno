from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='sistema.index'),
    url(r'^login/$', views.login_view, name='sistema.login'),
	url(r'^logout$', views.logout_view, name='sistema.logout'),
    url(r'^consulta$', views.consulta_view, name='sistema.consulta'),
    url(r'^signup$', views.UserFormView.as_view(), name='sistema.register'),
    url(r'^pago$', views.ServiciosView.as_view(), name='sistema.pago'),
    url(r'^credito$', view=views.CreditosView.as_view(), name='sistema.creditos'),
    url(r'^debito$', view=views.DebitosView.as_view(), name='sistema.debitos'),
    url(r'^transferencia$', views.TransferenciaView.as_view(), name='sistema.transferencias'),
]