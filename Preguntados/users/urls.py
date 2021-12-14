from django.conf.urls import url
from django.urls import path
from .views import login_view, logout_view, PreguntadosLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('login/', login_view, name='login-view'),
    path('login/', PreguntadosLoginView.as_view(), name='login-view'),
    #path('logout/', logout_view, name='logout-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
]