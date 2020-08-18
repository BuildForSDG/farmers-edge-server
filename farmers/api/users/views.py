from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token_generator import account_activation_token
# Create your views here.
def activate_account(request,  uidb64, token):
    # import pdb; set_trace()
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user,token)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        print("usr",user)
        user.is_active = True
        user.save()
        return HttpResponse('Your account has been activated successfully')
    else:
        return HttpResponse('Activation link is invalid!')
def confirm_update(request,uidb64,token):
    if 'password' in request.GET and request.GET["password"]:
        password = request.GET.get('password')
        print(password)
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            print(user,token)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            print("usr",user)
            user.set_password(password)
            user.save()
            return HttpResponse({"You have reset your password successfully"})
        else:
            return HttpResponse({"Invalid token"})
    return render(request,'change/pass_change.html')
        # return Response("hey")
# def reset_password(request, uidb64, token):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#         print(user,token)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         print(user)
#         user.is_active = True
#         user.save()
#         return HttpResponse('Your account has been activate successfully')
#     else:
#         return HttpResponse('Activation link is invalid!')