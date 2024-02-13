from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm


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
            # message_from_bytes.warning(request, "Incorrect Credentials")
            return redirect('/')
        
    return render(request, 'login.html', context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
      
    
    return render(request, "register.html", context)




