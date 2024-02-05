import uuid
import threading
import time
from django.http import HttpResponse
from ..models import SuzdalUser
from ..util.suzdal_response import JR
from django.core.mail import EmailMessage
from django.http import HttpResponse


def createUser(request):
    user_token = str(uuid.uuid4())
    userEmail = request.POST.get('user_email', 'none') # alexey.saron@gmail.com
    
    if userEmail != 'none':
        index1 = userEmail.find('@')
        index2 = userEmail.find('.')
        
        if index1 != -1 and index2 != -1:
            suzdal_user = SuzdalUser.objects.get_or_create(email=userEmail)[0]
            link = '?email='+userEmail+'&token='+user_token+'&id='+str(suzdal_user.id)
            mail_sent = send_email(userEmail, link)   
            
            if mail_sent == 1 or mail_sent == 'ok':
                suzdal_user.token = user_token
            suzdal_user.save()
            return JR({'response': 'Usuario Creado', 'id': suzdal_user.id})
    else:
        return JR({'response': 'error'})
    

# 192.168.51.166:5500/publicar-perfil/?email=alexey.saron@gmail.com&token=99b31467-216c-4c28-9b0d-eb3652bb91ff
def send_email(userEmail, link):
    subject        = 'MIS CITAS'
    from_email     = 'mis.citas.app@gmail.com'
    recipient_list = [userEmail, 'alexey.saron@gmail.com']
    html_message = '''
    <html>
        <body style="background-color: #fff8f4;">
            <div style="text-align: center; font-size: 22px;">
                <p>Inicia sesión en MIS CITAS y pública tu perfil</p>
                <a href="https://miscitas.eu/publicar-perfil/index.html'''+link+'''" target="_blank">
                    <input type="button" value="Login" style="background-color: #E36831; padding: 11px; border: none; border-radius: 4px; color:white; font-size: 22px;">
                </a>
            </div>
        </body>
    </html>
    '''
    email = EmailMessage(subject, html_message, from_email, recipient_list)
    email.content_subtype = 'html'
    return email.send()
    




def loginFunction(request):
    user_id    = str(request.POST.get('id', 'none')).strip()
    user_email = request.POST.get('email', 'none').strip()
    user_token = request.POST.get('token', 'none').strip()

    if user_id != 'none' and user_email != 'none' and user_token != 'none':
        try:
            # Start a new thread
            # param1 = 'Hello'
            # param2 = 'World'
            # thread = threading.Thread(target=background_task, args=(param1, param2))
            # thread.start()
            
            suzdal_user = SuzdalUser.objects.get(id=user_id)
            if suzdal_user.token == user_token:
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
                return  JR({'response': 'Login Controller false creadentials'+suzdal_user.token})
        except Exception as e:
            return  JR({'response': 'Login Controller false user '+ str(e)})
    else:
        return  JR({'response': 'Login Controller empty request'})
    


def background_task(arg1, arg2):
    time.sleep(900)
    print(arg1, arg2)
    pass

   
