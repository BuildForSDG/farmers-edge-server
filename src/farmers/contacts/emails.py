from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_issue_tracking(name,receiver):
    subject ='Your issue has been noted'
    sender = 'emmanuelthedeveloper@gmail.com'

    text_content = render_to_string('email/contact.txt',{"name":name})
    html_content = render_to_string('email/contact.html',{"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()