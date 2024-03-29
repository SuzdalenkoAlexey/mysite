from django.urls import path
from . import views
from .controllers.LoginController import createUser, loginFunction
from .controllers.ProfileController import saveUserData, activateProfile
from .controllers.BuserController import getOnlyUser
from .controllers.GoodController import getGoodUsers, getListUserImages

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', createUser),
    path('login/', loginFunction),
    path('save_user_data/', saveUserData),
    path('getOnlyUser/', getOnlyUser),
    path('getGoodUsers/', getGoodUsers),
    path('activateProfile/', activateProfile),
    path('getListUserImages/', getListUserImages)
    
]