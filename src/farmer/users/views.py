from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from users.forms import AccountAuthenticationForm



def login_view(request):
	context = {}
	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
		if user:
			login(request, user)
			return redirect('home')
	else:
		form = AccountAuthenticationForm()
		context['login_form'] = form
	return render(request, "users/login.html", context)

def home_screen_view(request):
	if not request.user.is_authenticated:
			return redirect("login")

	return render(request, "users/home.html", {})


