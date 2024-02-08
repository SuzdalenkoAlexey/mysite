from django.db import connection
from ..models import SuzdalUser
from ..util.suzdal_response import JR, UP


def getOnlyUser(request):
    userId = request.GET.get('id', 0)
    try:
        suzdal_user = SuzdalUser.objects.get(id=userId)
        return  UP(suzdal_user)
    except:
        return JR({'error':'not found user BuserController'})
