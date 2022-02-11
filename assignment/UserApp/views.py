from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.

def homeView(request):
	authenticated = request.user.is_authenticated
	if authenticated:
			postForm = user_post_form()
	context = {
		'postForm':postForm,
	}
	return render(request, 'home.html', context)

def postSubmitView(request):
	redirectTo = request.POST.get('redirectTo')
	if request.method == 'POST':
		addPost = user_post_form(request.POST)
		if addPost.is_valid():
			cd = addPost.save(commit=False)
			cd.save()
			messages.success(request, 'Product is added Successfully')
		else:
			messages.error(request, 'Wrong Input Data, Please check An Error occurred')
	return redirect(redirectTo)

