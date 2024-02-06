from django.shortcuts import render, redirect
from . form import IncomingMailsForm, OutgoingMailsForm, FilesForm
from . models import IncomingMail,  OutGoingMail, BaseAttachments
# from . models import RecModel, OutgoingModel
from django.db.models import Q  
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

    return render(request, 'records/signup.html')

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
        
    return render(request, 'records/signin.html')

#-------------------------------End signin module-------------------------------#


#-------------------------------signout module-------------------------------#

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('/')


#-------------------------------End signout module-------------------------------#
  



#-------------------------------Homepage module-------------------------------#

def home(request):
    return render(request, 'records/home.html')



#-------------------------------incoming mails module-------------------------------#

def records_form(request, id=0):
    # for rendering the actual form from the form.py

    if request.method == 'GET':
        if id == 0:
            rec_details = IncomingMailsForm()
        else:
            rec_from_db = IncomingMail.objects.get(pk=id)
            rec_details = IncomingMailsForm(instance=rec_from_db)
            
        context = {'records': rec_details}
        return render(request, 'records/mailsform.html', context)
    
    
    else:
        # for saving the details keyed from the form into the database
        if id ==0:
            rec_details = IncomingMailsForm(request.POST)
        # updates the details brought on the form by id
        else:
            rec_to_update = IncomingMail.objects.get(pk=id)
            rec_details = IncomingMailsForm(request.POST, instance=rec_to_update)
        if rec_details.is_valid():
            rec_details.save()

        return redirect('/incominglist')
    
# for displaying and searching details from the database to the user interface
def records_list(request):
    # for search operation
    if 'q' in request.GET:
        q= request.GET['q']
        # records = RecModel.objects.filter(sender__icontains = q)
        multiple_q = Q(Q(sender__icontains = q) | Q(subject__icontains = q))
        records = IncomingMail.objects.filter(multiple_q)
    else:
        records = IncomingMail.objects.all()
    context = {'records': records}
    return render(request, 'records/mailslist.html', context)


# for deleting records chosen
def records_delete(request, id):
    record_to_delete = IncomingMail.objects.get(pk=id)
    record_to_delete.delete()

    return records_list(request)

#-------------------------------End incoming mails module-------------------------------#


        
#-------------------------------outgoing mails module-------------------------------#

def outgoing_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            outgoing_recs = OutgoingMailsForm()
        else:
            record_details = OutGoingMail.objects.get(pk=id)
            outgoing_recs = OutgoingMailsForm(instance = record_details)

        context = {
            'records': outgoing_recs
        }
        return render(request, 'records/outgoingform.html', context)

    else:
        if id == 0:
            outgoing_recs =  OutgoingMailsForm(request.POST)
        else:
            record_details = OutGoingMail.objects.get(pk=id)
            outgoing_recs = OutgoingMailsForm(request.POST, instance = record_details)

        if outgoing_recs.is_valid():
            outgoing_recs.save()

        return redirect('/outgoinglist')
    


def outgoing_list(request):
    if 'q' in request.GET:
        q= request.GET['q']
        # records = RecModel.objects.filter(sender__icontains = q)
        multiple_q = Q(Q(sender__icontains = q) | Q(mail_destination_icontains = q) | Q(subject__icontains = q))
        outgoing_recs = OutGoingMail.objects.filter(multiple_q)
    else:
        outgoing_recs = OutGoingMail.objects.all()
    context = {
        'outgoing_list': outgoing_recs
    }

    return render(request, 'records/outgoinglist.html', context)


def delete_outgoing(request, id):
    rec_to_delete = OutGoingMail.objects.get(pk=id)
    rec_to_delete.delete() 

    return outgoing_list(request)





#-------------------------------Files module-------------------------------#

def files_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            files_rec = FilesForm()
        else:
            files_details = BaseAttachments.objects.get(pk=id)
            files_rec = FilesForm(instance = files_details)

        context = {
            'files': files_rec
        }
        return render(request, 'records/filesform.html', context)

    else:
        if id == 0:
            files_rec =  FilesForm(request.POST)
        else:
            files_details = BaseAttachments.objects.get(pk=id)
            files_rec = FilesForm(request.POST, instance = files_details)

        if files_rec.is_valid():
            files_rec.save()

        return redirect('/fileslist')
    
def files_list(request):
    if 'q' in request.GET:
        q= request.GET['q']
        # records = RecModel.objects.filter(sender__icontains = q)
        multiple_q = Q(Q(mail_sender__icontains = q) | Q(mail_receiver__icontains = q) | Q(subject__icontains = q))
        files_rec = BaseAttachments.objects.filter(multiple_q)
    else:
        files_rec = BaseAttachments.objects.all()
    context = {
        'files_list': files_rec
    }

    return render(request, 'records/fileslist.html', context)


def delete_file(request, id):
    file_to_delete = BaseAttachments.objects.get(pk=id)
    file_to_delete.delete() 

    return files_list(request)

















# #-------------------------------signup module-------------------------------#
# def signup(request):
#     if request.method == 'POST':
#         # username = request.POST.get('Username')
#         uname = request.POST['Username']
#         fname = request.POST['Firstname']
#         lname = request.POST['Lastname']
#         email = request.POST['Email']
#         password1 = request.POST['Password1']
#         conf_password = request.POST['Password2']

        
#         myuser = User.objects.create_user(uname,email, password1)
#         myuser.first_name=fname
#         myuser.last_name = lname
#         myuser.save()
#         messages.success(request, "Your account has been created")
#         return redirect('/')

#     return render(request, 'records/signup.html')

# #-------------------------------End signup module-------------------------------#

# #-------------------------------signin module-------------------------------#

# def signin(request):
#     if request.method =='POST':
#         uname = request.POST['Username']
#         password1 = request.POST['Password1']

#         user = authenticate(username=uname, password=password1)


#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             return render(request, 'records/home.html', {'fname': fname})
#         else:
#             messages.warning(request, "Incorrect Credentials")
#             return redirect('/')
        
#     return render(request, 'records/signin.html')

# #-------------------------------End signin module-------------------------------#


# #-------------------------------signout module-------------------------------#

# def signout(request):
#     logout(request)
#     messages.success(request, "Logged out Successfully!")
#     return redirect('/')


# #-------------------------------End signout module-------------------------------#
  



# #-------------------------------Homepage module-------------------------------#

# def home(request):
#     return render(request, 'records/home.html')



# #-------------------------------incoming mails module-------------------------------#

# def records_form(request, id=0):
#     # for rendering the actual form from the form.py

#     if request.method == 'GET':
#         if id == 0:
#             rec_details = RecForm()
#         else:
#             rec_from_db = RecModel.objects.get(pk=id)
#             rec_details = RecForm(instance=rec_from_db)
            
#         context = {'records': rec_details}
#         return render(request, 'records/mailsform.html', context)
    
    
#     else:
#         # for saving the details keyed from the form into the database
#         if id ==0:
#             rec_details = RecForm(request.POST)
#         # updates the details brought on the form by id
#         else:
#             rec_to_update = RecModel.objects.get(pk=id)
#             rec_details = RecForm(request.POST, instance=rec_to_update)
#         if rec_details.is_valid():
#             rec_details.save()

#         return redirect('list/')
    
# # for displaying and searching details from the database to the user interface
# def records_list(request):
#     # for search operation
#     if 'q' in request.GET:
#         q= request.GET['q']
#         # records = RecModel.objects.filter(sender__icontains = q)
#         multiple_q = Q(Q(sender__icontains = q) | Q(subject__icontains = q))
#         records = RecModel.objects.filter(multiple_q)
#     else:
#         records = RecModel.objects.all()
#     context = {'records': records}
#     return render(request, 'records/mailslist.html', context)


# # for deleting records chosen
# def records_delete(request, id):
#     record_to_delete = RecModel.objects.get(pk=id)
#     record_to_delete.delete()

#     return records_list(request)

# #-------------------------------End incoming mails module-------------------------------#


        
# #-------------------------------outgoing mails module-------------------------------#

# def outgoing_form(request, id=0):
#     if request.method == 'GET':
#         if id == 0:
#             outgoing_recs = OutgoingMailsForm()
#         else:
#             record_details = OutgoingModel.objects.get(pk=id)
#             outgoing_recs = OutgoingMailsForm(instance = record_details)

#         context = {
#             'records': outgoing_recs
#         }
#         return render(request, 'records/outgoingform.html', context)

#     else:
#         if id == 0:
#             outgoing_recs =  OutgoingMailsForm(request.POST)
#         else:
#             record_details = OutgoingModel.objects.get(pk=id)
#             outgoing_recs = OutgoingMailsForm(request.POST, instance = record_details)

#         if outgoing_recs.is_valid():
#             outgoing_recs.save()

#         return redirect('/outgoinglist')
    


# def outgoing_list(request):
#     if 'q' in request.GET:
#         q= request.GET['q']
#         # records = RecModel.objects.filter(sender__icontains = q)
#         multiple_q = Q(Q(mail_sender__icontains = q) | Q(mail_receiver__icontains = q) | Q(subject__icontains = q))
#         outgoing_recs = OutgoingModel.objects.filter(multiple_q)
#     else:
#         outgoing_recs = OutgoingModel.objects.all()
#     context = {
#         'outgoing_list': outgoing_recs
#     }

#     return render(request, 'records/outgoinglist.html', context)


# def delete_outgoing(request, id):
#     rec_to_delete = OutgoingModel.objects.get(pk=id)
#     rec_to_delete.delete() 

#     return outgoing_list(request)






