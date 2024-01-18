from django.urls import path
from . import views
from .controllers.LoginController import loginFunction

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", loginFunction)
]