from django.urls import path
from . import views
from .controllers.LoginController import createUser, loginFunction

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', createUser),
    path('login/', loginFunction),


    
]