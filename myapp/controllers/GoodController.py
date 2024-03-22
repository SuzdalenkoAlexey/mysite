from django.db import connection
from ..util.suzdal_response import JR
from ..models import SuzdalImage

def getGoodUsers(request):
    slq = """SELECT id, province, category, city, name, age, cover_image
             FROM suzdal_user 
             WHERE state = 1
             ORDER BY id DESC
          """
    cursor = connection.cursor()
    cursor.execute(slq)
    out_data = []
    res = cursor.fetchall()
    for r in res:
        x = {'id':r[0], 'province':r[1], 'category':r[2], 'city':r[3], 'name':r[4], 'age':r[5], 'cover_image':r[6]}
        out_data += [x]
    cursor.close()
    # que mas pasa
    return JR({'res':out_data})


def getListUserImages(request):
    try:
        userId = request.GET.get('id', 0)
        imgs = SuzdalImage.objects.get(id=userId)
        res = [imgs.image1, imgs.image2, imgs.image3, imgs.image4, imgs.image5, imgs.image6]
        return JR({'id': userId, 'res': res})
    except:
        return JR({'id': userId, 'res': None})