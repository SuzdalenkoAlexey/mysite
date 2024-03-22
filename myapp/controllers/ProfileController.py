from ..util.suzdal_response import JR, UP
from ..models import SuzdalImage, SuzdalUser
import base64
from io import BytesIO
from PIL import Image, ExifTags


def saveUserData(request):
    userId    = request.POST.get('id')
    userToken = str(request.POST.get('token', 'none')).strip()
    try:
        suzdal_user = SuzdalUser.objects.get(id=userId)
        if suzdal_user.token == userToken:
            suzdal_user.province    = str(request.POST.get('province', '')).strip()
            suzdal_user.category    = str(request.POST.get('category', '')).strip()
            suzdal_user.city        = str(request.POST.get('city', '')).strip()
            suzdal_user.zone        = str(request.POST.get('zone', '')).strip()
            suzdal_user.name        = str(request.POST.get('name', '')).strip()
            suzdal_user.age         = str(request.POST.get('age', '')).strip()
            suzdal_user.phone       = str(request.POST.get('phone', '')).strip()
            suzdal_user.page_title  = str(request.POST.get('page_title', '')).strip()
            suzdal_user.about_me    = str(request.POST.get('about_me', '')).strip()
            dataImage               = str(request.POST.get('cover_image', ''))
            if len(dataImage) > 111:
                suzdal_user.cover_image = fun_pre_save_img(dataImage)
            suzdal_user.save()

            # save list user images
            suzdal_image = SuzdalImage.objects.get_or_create(user_id=suzdal_user.id)[0]
            if len(str(request.POST.get('img1', ''))) > 111: suzdal_image.image1 = fun_pre_save_img(request.POST.get('img1', ''))
            if len(str(request.POST.get('img2', ''))) > 111: suzdal_image.image2 = fun_pre_save_img(request.POST.get('img2', ''))
            if len(str(request.POST.get('img3', ''))) > 111: suzdal_image.image3 = fun_pre_save_img(request.POST.get('img3', ''))
            if len(str(request.POST.get('img4', ''))) > 111: suzdal_image.image4 = fun_pre_save_img(request.POST.get('img4', ''))
            if len(str(request.POST.get('img5', ''))) > 111: suzdal_image.image5 = fun_pre_save_img(request.POST.get('img5', ''))
            if len(str(request.POST.get('img6', ''))) > 111: suzdal_image.image6 = fun_pre_save_img(request.POST.get('img6', ''))
            suzdal_image.save()
            return  UP(suzdal_user)
        else:
            print("NO ENCONTRADO")
            return JR({'error':'token false'})
    except Exception as e:
        print("An error occurred: "+str(e))
        return JR({'error':str(e)})
    

def fun_pre_save_img(dataImage):
    compressed = ""
    extensionA = dataImage.split(",")[0]
    if 'jpeg' in extensionA:
        compressed = compress_and_encode_image(dataImage)
    elif 'png' in extensionA:
        compressed = convert_png_to_jpg_base64(dataImage)
    
    print("simbols="+str(len(dataImage)))
    print("simbols="+str(len(compressed)))
    return compressed

  
    

    
def compress_and_encode_image(base64_data, quality=22):
        img_data = base64.b64decode(base64_data.split(",")[1])
        image = Image.open(BytesIO(img_data))

        for orientation in ExifTags.TAGS.keys():
            if image._getexif() != None:
                if ExifTags.TAGS[orientation] == 'Orientation':
                    exif_data = dict(image._getexif().items())
                    if orientation in exif_data:
                        if exif_data[orientation] == 3:
                            image = image.rotate(180, expand=True)
                        elif exif_data[orientation] == 6:
                            image = image.rotate(270, expand=True)
                        elif exif_data[orientation] == 8:
                            image = image.rotate(90, expand=True)
        compressed_img_io = BytesIO()
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(compressed_img_io, format='JPEG', quality=quality)
        compressed_base64_data = "data:image/jpeg;base64,"+base64.b64encode(compressed_img_io.getvalue()).decode('utf-8')
        return compressed_base64_data


def convert_png_to_jpg_base64(base64_data, quality=22):
        img_data = base64.b64decode(base64_data.split(",")[1])
        image = Image.open(BytesIO(img_data))
        converted_img_io = BytesIO()
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(converted_img_io, format='JPEG', quality=quality)
        converted_base64_data = "data:image/jpeg;base64," + base64.b64encode(converted_img_io.getvalue()).decode('utf-8')
        return converted_base64_data



def activateProfile(request):
    userId = request.POST.get('id', '').strip()
    userTk = request.POST.get('token', '').strip()
    try:
        suzdal_user = SuzdalUser.objects.get(id=userId)
        if suzdal_user.token == userTk:
            suzdal_user.state = 1
            suzdal_user.save()
            return UP(suzdal_user)
        else:
            return JR({'error':'user no found'})
    except Exception as e:
        return JR({'error':str(e)})