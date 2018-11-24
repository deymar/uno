from django.views import generic
from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .forms import ContactUsuarioLoginForm

# Create your views here.
class AboutView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home/about.html')

class BienvenidaView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home/bienvenida.html')