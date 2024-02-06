from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#-------------------------------signup module-------------------------------#
def signup(request):
    if request.method == 'POST':
        # username = request.POST.get('Username')
        uname = request.POST['Username']
        fname = request.POST['Firstname']
        lname = request.POST['Lastname']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        conf_password = request.POST['Password2']

        
        myuser = User.objects.create_user(uname,email, password1)
        myuser.first_name=fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been created")
        return redirect('/')

    return render(request, 'users/signup.html')

#-------------------------------End signup module-------------------------------#

#-------------------------------signin module-------------------------------#

def signin(request):
    if request.method =='POST':
        uname = request.POST['Username']
        password1 = request.POST['Password1']

        user = authenticate(username=uname, password=password1)


        if user is not None:
            login(request, user)
            fname = user.first_name 
            return render(request, 'records/home.html', {'fname': fname})
        else:
            messages.warning(request, "Incorrect Credentials")
            return redirect('/')
        
    return render(request, 'users/signin.html')

#-------------------------------End signin module-------------------------------#


#-------------------------------signout module-------------------------------#

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('/')


#-------------------------------End signout module-------------------------------#
  

