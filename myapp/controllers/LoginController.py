import uuid
import threading
import time
from django.http import HttpResponse
from ..models import SuzdalUser
from ..util.suzdal_response import JR

def loginFunction(request):

    reg_email = request.GET.get('email', 'none')
    req_token = request.GET.get('token', 'none')

    if reg_email != 'none' and req_token != 'none':
        try:
            # Start a new thread
            param1 = 'Hello'
            param2 = 'World'
            thread = threading.Thread(target=background_task, args=(param1, param2))
            thread.start()
            
            suzdal_user = SuzdalUser.objects.get(email=reg_email)
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
    


def background_task(arg1, arg2):
    time.sleep(900)
    print(arg1, arg2)
    pass

   
