from django.shortcuts import render, redirect
from . form import IncomingMailsForm, OutgoingMailsForm, FilesForm, FileMovementForm
from . models import IncomingMail,  OutGoingMail, BaseAttachments, FileMovement
# from . models import RecModel, OutgoingModel
from django.db.models import Q  



#-------------------------------Homepage module-------------------------------#

def home(request):
    return render(request, 'records/home.html')



#-------------------------------incoming mails module--------------------------#

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
        multiple_q = Q(Q(sender__icontains = q) | Q(description__icontains = q))
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
        multiple_q = Q(Q(sender__icontains = q) | Q(mail_destination_icontains = q) | Q(description__icontains = q))
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
        multiple_q = Q(Q(name__icontains = q) | Q(category__icontains = q))
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


#-------------------------------End Files module-------------------------------#




#-------------------------------File movement module-------------------------------#

def file_movement(request, id=0):
    if request.method == 'GET':
        if id == 0:
            file_movement_rec = FileMovementForm()
        else:
            files_details = FileMovement.objects.get(pk=id)
            file_movement_rec = FileMovementForm(instance = files_details)

        context = {
            'fileMovement': file_movement_rec
        }
        return render(request, 'records/fileMovement.html', context)

    else:
        if id == 0:
            file_movement_rec =  FileMovementForm(request.POST)
        else:
            files_details = FileMovement.objects.get(pk=id)
            file_movement_rec = FileMovementForm(request.POST, instance = files_details)

        if file_movement_rec.is_valid():
            file_movement_rec.save()

        return redirect('/filemovementlist')
    
def files_movement_list(request):
    if 'q' in request.GET:
        q= request.GET['q']
        # records = RecModel.objects.filter(sender__icontains = q)
        multiple_q = Q(Q(collected_by__icontains = q) | Q(destination_office__icontains = q))
        files_rec = FileMovement.objects.filter(multiple_q)
    else:
        files_rec = FileMovement.objects.all()
    context = {
        'file_movement_list': files_rec
    }

    return render(request, 'records/fileMovList.html', context)


# def delete_file(request, id):
#     file_to_delete = FileMovement.objects.get(pk=id)
#     file_to_delete.delete() 

#     return files_list(request)


#-------------------------------End File movement module-------------------------------#

