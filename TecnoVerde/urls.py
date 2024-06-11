from django.contrib.auth import views as auth_views
from django.urls import path
from .views import logout_user
from TecnoVerde import views

from .forms import LoginForm

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contaminacion/', views.contaminacion, name='contaminacion'),
    path('ss/', views.ss, name='ss'),
    path('alternativas/', views.alternativas, name='alternativas'),
    path('signup/', views.signup, name= 'signup'),
    path('index3/', views.index3, name= 'index3'),
    path('login/', auth_views.LoginView.as_view(template_name='TecnoVerde/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', logout_user, name='logout'),
    
]