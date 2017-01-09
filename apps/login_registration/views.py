from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User
# Create your views here.
def index(request):
	return render(request, 'login_registration/index.html')
def login(request):
	if request.method == "POST":
		user = User.objects.login(request.POST)
		if not user:
			messages.error(request, "Invalid login credentials!")
		else:
			request.session['logged_user'] = user.id
			messages.success(request, "Welcome {}!".format(user.name))
			return redirect(reverse('travels:travel'))
	return redirect('/')

def success(request):
	if 'logged_user' not in request.session:
		return redirect('/')
	context = {
		'user' : User.objects.get(id=request.session['logged_user'])
	}
	return redirect(reverse(request, 'travels:travel'))

def register(request):
	if request.method == "POST":
		form_errors = User.objects.validate_user_info(request.POST)

		if len(form_errors) > 0:
			for error in form_errors:
				messages.error(request, error)
		else:
			User.objects.register(request.POST)
			messages.success(request, "You have successfully registered, please sign in to continue")
	return redirect('/')

def logout(request):
	if 'logged_user' in request.session:
		request.session.pop('logged_user')
	return redirect('/')