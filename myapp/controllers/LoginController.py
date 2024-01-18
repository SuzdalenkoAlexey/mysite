import uuid
from django.http import HttpResponse
from ..models import SuzdalUser
from ..util.suzdal_response import JR

def loginFunction(request):

    reg_email = request.GET.get('email', 'none')
    req_token = request.GET.get('token', 'none')

    if reg_email != 'none' and req_token != 'none':
        try:
            suzdal_user = SuzdalUser.objects.get_or_create(email=reg_email)
            if suzdal_user.token == req_token:
                # user login
                suzdal_user.uid = str(uuid.uuid4())
                suzdal_user.save()

                return  JR({'response': 'Login Controller false creadentials '+suzdal_user.id })
            else:
                return  JR({'response': 'Login Controller false creadentials'})
        except:
            return  JR({'response': 'Login Controller false user'})
    else:
        return  JR({'response': 'Login Controller empty request'})

   
