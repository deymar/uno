from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile, PagoServicio
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    password = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        def save(self, commit=True):
            user = super(UserCreateForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user

class RegistroForm(forms.Form):
    username=forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['user', 'nombre', 'correo', 'password']

class PagoServicioForm(forms.ModelForm):
    
    class Meta:
        model = PagoServicio
        fields = ('cuenta_servicio', 'tipo_servicio', 'monto')
        labels = {
            'cuenta_servicio': 'Cuenta del servicio',
            'tipo_servicio': 'Tipo de servicio',
            'monto': 'Monto',
        }

        widgets = {
            'cuenta_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_serivicio': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }
