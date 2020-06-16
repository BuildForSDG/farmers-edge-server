from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .token_generator import account_activation_token
from django.conf import settings

def send_welcome_email(name,receiver,uid,b,token):
    #creating the message,subject and sender
    subject = "Activate your account"
    sender = settings.EMAIL_HOST_USER

    # @passing in the context variables
    text_content = render_to_string('email/newsemail.txt',{"name":name,"uid":uid,"b":b,"token":token})
    html_content = render_to_string('email/newsemail.html',{"name":name,"uid":uid,"b":b,"token":token})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    # import pdb; pdb.set_trace()
    msg.send()

def send_password_reset_token(name,receiver,uid,b,token):
    subject = "Reset your password"
    sender = settings.EMAIL_HOST_USER
    text_content = render_to_string('email/resets.txt',{"name":name,"uid":uid,"b":b,"token":token})
    html_content = render_to_string('email/resets.html',{"name":name,"uid":uid,"b":b,"token":token})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

