from django.urls import path
from django.urls import reverse_lazy
from django.conf.urls import url
from .views import logout, login, signup
from .views import password_reset_complete, password_reset_done

app_name = 'users'


urlpatterns = [
    path('logout/' , logout, name='logout'),
    path('login' , login, name='login'),
    path('signup/' , signup, name='signup') 
]
