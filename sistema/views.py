
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import UserProfile, PagoServicio, Credito, Debito, Transferencia
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView
from django.forms import ModelForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserProfileForm, PagoServicioForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from decimal import Decimal

# Create your views here.
@login_required
def index_view(request):
	return render(request, 'sistema/index.html')

@login_required
def consulta_view(request):
	return render(request, 'sistema/consulta.html')

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('sistema.index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('sistema.index'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        mensaje = 'Nombre de usuario o contrasena no valido'
    return render(request, 'sistema/login.html', {'mensaje': mensaje})

def logout_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('sistema.login'))

class UserFormView(generic.View):
    form_class = UserCreateForm
    template_name = 'sistema/registration.html'

class CreditosView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'sistema/credito.html')


    def post(self, request, *args, **kwargs):
        monto = request.POST['monto']
        usuario = request.POST['username']
        descripcion = request.POST['desc']
        user = UserProfile.objects.get(codigo=request.POST['username'])
        user.saldo = user.saldo + Decimal(monto)
        messages.success(request, 'El monto ha sido acreditado exitosamente.')
        p = Credito(user_cuenta = user, monto = monto, descripcion = descripcion)
        p.save()
        user.save()
        return render(request, 'sistema/credito.html')

class TransferenciaView(generic.View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'sistema/transferencias.html')

    def post(self, request, *args, **kwargs):
        username = None 
        if request.user.is_authenticated():
            username = request.user.username
        monto = request.POST['monto']
        user1 = UserProfile.objects.get(codigo=request.POST['username'])
        user2 = UserProfile.objects.get(user = request.user)

        if user2.saldo > Decimal(monto):
            user1.saldo = user1.saldo + Decimal(monto)
            user1.save()
            user2.saldo = user2.saldo - Decimal(monto)
            user2.save()
            p = Transferencia(user_cuenta = user1.codigo, user_cuenta2 = user2.codigo, monto = Decimal(monto))
            p.save()
            messages.success(request, 'Transferencia de ' + monto + ' efectuada exitosamente')
        else :
            messages.error(request, 'Su saldo es menor al monto que desea transferir')
        return render(request, 'sistema/transferencias.html')

    

class ServiciosView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sistema/servicios.html')

    def post(self, request, *args, **kwargs):
        username = None 
        if request.user.is_authenticated():
            username = request.user.username
        cuenta = request.POST['cuenta_servicio']
        servicio = request.POST['tipo_servicio']
        monto = request.POST['monto']

        if self.request.user.userprofile.saldo >= Decimal(monto):
            self.request.user.userprofile.saldo = self.request.user.userprofile.saldo - Decimal(monto)
            p = PagoServicio(cuenta_servicio=cuenta, tipo_servicio=servicio, monto=monto, user_cuenta=request.user.userprofile.codigo)
            p.save()
            messages.success(request, 'El servicio ha sido pagado exitosamente')
        else:
            messages.success(request, 'El monto que se desea debitor es mayor al saldo de la cuenta.')

        return render(request, 'sistema/servicios.html')
        self.request.user.userprofile.save()

class DebitosView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'sistema/debito.html')

    def post(self, request, *args, **kwargs):
        monto = request.POST['monto']
        usuario = request.POST['username']
        descripcion = request.POST['desc']
        user = UserProfile.objects.get(codigo=request.POST['username'])
        print(user.saldo)
        print(monto)
        if user.saldo > Decimal(monto) :
            user.saldo = user.saldo - Decimal(monto)
            p = Debito(user_cuenta = user, monto = monto, descripcion = descripcion)
            p.save()
            messages.success(request, 'El monto se ha debitado exisotamente.')

        else :
            messages.error(request, 'El monto que se desea debitor es mayor al saldo de la cuenta.')        
       
       
        user.save()
        return render(request, 'sistema/debito.html')
