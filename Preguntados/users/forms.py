from django import forms
from .models import PreguntadosUser
from django.contrib.auth import authenticate


class UserForm(forms.Form):
    username = forms.CharField(max_length=25, label='Nombre de usuario')
    password = forms.CharField(max_length=25, widget=forms.PasswordInput(), label='Contraseña')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_username = PreguntadosUser.objects.filter(username=username).exists()
        user = authenticate(username=username, password=password)
        if not user:
            if not user_username:
                raise forms.ValidationError('El usuario no existe!!!')
            else:
                raise forms.ValidationError('Tu contraseña es incorrecta!!!')
        
        return self.cleaned_data