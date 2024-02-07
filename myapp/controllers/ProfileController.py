from ..util.suzdal_response import JR, UP
from ..models import SuzdalUser

def saveUserData(request):
    userId    = request.POST.get('id')
    userToken = str(request.POST.get('token', 'none')).strip()

    print(request.POST.get('category', ''))

    try:
        suzdal_user = SuzdalUser.objects.get(id=userId)
        if suzdal_user.token == userToken:
            suzdal_user.province   = str(request.POST.get('province', '')).strip()
            suzdal_user.category   = str(request.POST.get('category', '')).strip()
            suzdal_user.city       = str(request.POST.get('city', '')).strip()
            suzdal_user.zone       = str(request.POST.get('zone', '')).strip()
            suzdal_user.name       = str(request.POST.get('name', '')).strip()
            suzdal_user.age        = str(request.POST.get('age', '')).strip()
            suzdal_user.phone      = str(request.POST.get('phone', '')).strip()
            suzdal_user.page_title = str(request.POST.get('page_title', '')).strip()
            suzdal_user.about_me   = str(request.POST.get('about_me', '')).strip()

            suzdal_user.save()
            return  UP(suzdal_user)
        else:
            print("NO ENCONTRADO")
            return JR({'res':'token false'})
    except:
        print("NO ENCONTRADO")
        return JR({'res':'not found'})

    return  JR({
                'id':1
                })