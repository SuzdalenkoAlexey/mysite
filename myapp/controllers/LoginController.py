import uuid
import threading
import time
from datetime import datetime
from django.http import HttpResponse
from ..models import SuzdalUser
from ..util.suzdal_response import JR, UP
from django.core.mail import EmailMessage
from django.http import HttpResponse


def createUser(request):
    user_token = str(uuid.uuid4()).strip()
    userEmail = request.POST.get('user_email', 'none').strip() # alexey.saron@gmail.com
    
    if userEmail != 'none':
        index1 = userEmail.find('@')
        index2 = userEmail.find('.')
        
        if index1 != -1 and index2 != -1:
            suzdal_user = SuzdalUser.objects.get_or_create(email=userEmail)[0]
            link = '?email='+userEmail+'&token='+user_token+'&id='+str(suzdal_user.id)
            mail_sent = send_email(userEmail, link)   
            
            if mail_sent == 1 or mail_sent == 'ok':
                if suzdal_user.token == None:
                    suzdal_user.token = user_token
                if suzdal_user.first_login == None:
                    suzdal_user.first_login = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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
            suzdal_user = SuzdalUser.objects.get(id=user_id)
            suzdal_user.last_login  = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
           
            if suzdal_user.token == user_token and suzdal_user.email == user_email:
                suzdal_user.save()
                return  UP(suzdal_user)
            else:
                return  JR({'response': 'Login Controller false creadentials'})
        except Exception as e:
            return  JR({'response': 'Login Controller false user'})
    else:
        return  JR({'response': 'Login Controller empty request'})
    

   
