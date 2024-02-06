from ..util.suzdal_response import JR
from ..models import SuzdalUser

def saveUserData(request):
    userId    = request.POST.get('id')
    userToken = str(request.POST.get('token', 'none')).strip()

    print(request.POST.get('category', ''))

    try:
        suzdal_user = SuzdalUser.objects.get(id=userId)
        if suzdal_user.token == userToken:
            suzdal_user.province = str(request.POST.get('province', '')).strip()
            suzdal_user.category = str(request.POST.get('category', '')).strip()
            suzdal_user.save()
            return  JR({
                    'id': suzdal_user.id,
                    'province': suzdal_user.province,
                    'zone':suzdal_user.zone,
                    'category': suzdal_user.category,
                    'city': suzdal_user.city,
                    'name': suzdal_user.name,
                    'age': suzdal_user.age,
                    'phone': suzdal_user.phone,
                    'page_title': suzdal_user.page_title,
                    'about_me': suzdal_user.about_me,
                    'cover_image': suzdal_user.cover_image
                })
        else:
            print("NO ENCONTRADO")
            return JR({'res':'token false'})
    except:
        print("NO ENCONTRADO")
        return JR({'res':'not found'})

    return  JR({
                'id':1
                })