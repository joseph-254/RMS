from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages, auth
from recProject import settings
from django.core.mail import send_mail


# from django.contrib.auth.models import auth

# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     if form.is_valid():
#         email  = form.cleaned_data.get('email')
#         password  = form.cleaned_data.get('password')
#         user = authenticate(request, username=email, password=password)
   
#         if user is not None:
#             login(request, user)
#             # auth.login(request, user)
        
#             return render(request, 'records/home.html', context)
#         else:
#             messages.warning(request, "Incorrect Credentials")
#             return redirect('/')
        
#     return render(request, 'users/login.html', context)


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return redirect('home/')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('/')
    return render(request, 'users/login.html')


# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     if form.is_valid():
#         form.save()
      
    
#     return render(request, "users/register.html", context)


#-------------------------------signup module-------------------------------#

User = get_user_model()
def register_page(request):
    if request.method == 'POST':
        # username = request.POST.get('Username')
        email = request.POST['Email']
        uname = request.POST['Username'] 
        password1 = request.POST['Password1']
        conf_password = request.POST['Password2']

        if User.objects.filter(username=uname):
            messages.error(request, "Username already exist! Please try using another username")  
            return render(request, 'users/register.html') 
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return render(request, 'users/register.html')
        
        if len(uname)>10:
            messages.error(request, "Username must be under 10 characters")
            return render(request, 'users/register.html')

        if password1 != conf_password:
            messages.error(request, "Passwords did not match!")
            return render(request, 'users/register.html')

        else:
        
            myuser = User.objects.create_user(email,uname, password1)
            myuser.username = uname
            myuser.save()
            messages.success(request, "Your account has been created, check your email for verification")


            # Welcome Email
            subject = "welcome to the RMS!"
            message = "Hello" + myuser.username + "\n" + "Welcome to RMS!! \n Thank you for visiting our platform, please confirm your email address to activate your account"
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently= True)


            return redirect('/')

    return render(request, 'users/register.html')

#-------------------------------End signup module-------------------------------#


def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('/')

