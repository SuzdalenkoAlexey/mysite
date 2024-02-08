from django.urls import path
from . import views
from .controllers.LoginController import createUser, loginFunction
from .controllers.ProfileController import saveUserData
from .controllers.BuserController import getOnlyUser

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', createUser),
    path('login/', loginFunction),
    path('save_user_data/', saveUserData),
    path('getOnlyUser/', getOnlyUser)

    
]