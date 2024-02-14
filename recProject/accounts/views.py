from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm
from django.contrib import messages


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        email  = form.cleaned_data.get('email')
        password  = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
   
        if user is not None:
            login(request, user)
        
            return render(request, 'index.html', context)
        else:
            messages.warning(request, "Incorrect Credentials")
            return redirect('/')
        
    return render(request, 'users/login.html', context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
      
    
    return render(request, "users/register.html", context)




