from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView


def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home-view'))
    else:
        form = UserForm()

    return render(request, 'users/login.html', {'form': form})


class PreguntadosLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def logout_view(request):
    logout(request)
    return redirect(reverse('login-view'))