from django.http import JsonResponse


def JR(x):
    jsonResponse = JsonResponse(x)
    jsonResponse["Access-Control-Allow-Origin"] = "*"
    jsonResponse["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    jsonResponse["Access-Control-Max-Age"] = "1000"
    # jsonResponse["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return jsonResponse


def UP(userModel):
    x = {
        'id': userModel.id,
        'province': userModel.province,
        'zone':userModel.zone,
        'category': userModel.category,
        'city': userModel.city,
        'name': userModel.name,
        'age': userModel.age,
        'phone': userModel.phone,
        'page_title': userModel.page_title,
        'about_me': userModel.about_me,
        'state': userModel.state,
        'cover_image': userModel.cover_image
    }
    jsonResponse = JsonResponse(x)
    jsonResponse["Access-Control-Allow-Origin"] = "*"
    jsonResponse["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    jsonResponse["Access-Control-Max-Age"] = "1000"
    return jsonResponse