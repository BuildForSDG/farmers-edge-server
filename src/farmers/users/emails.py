from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from .token_generator import account_activation_token

def send_welcome_email(name,receiver,uid,token):
    #creating the message,subject and sender
    subject = "Activate your account"
    sender = "levy.naibei91@gmail.com"

    # @passing in the context variables
    text_content = render_to_string('email/newsemail.txt',{"name":name,"uid":uid,"token":token})
    html_content = render_to_string('email/newsemail.html',{"name":name,"uid":uid,"token":token})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()