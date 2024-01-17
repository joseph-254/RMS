from django.shortcuts import render, redirect
from . form import RecForm
from . models import RecModel
from django.db.models import Q

# Create your views here.

def records_form(request, id=0):
    # for rendering the actual form from the form.py

    if request.method == 'GET':
        if id == 0:
            rec_details = RecForm()
        else:
            rec_from_db = RecModel.objects.get(pk=id)
            rec_details = RecForm(instance=rec_from_db)
            
        context = {'records': rec_details}
        return render(request, 'records/mailsform.html', context)
    
    
    else:
        # for saving the details keyed from the form into the database
        if id ==0:
            rec_details = RecForm(request.POST)
        # updates the details brought on the form by id
        else:
            rec_to_update = RecModel.objects.get(pk=id)
            rec_details = RecForm(request.POST, instance=rec_to_update)
        if rec_details.is_valid():
            rec_details.save()

        return redirect('list/')
    
# for displaying and searching details from the database to the user interface
def records_list(request):
    # for search operation
    if 'q' in request.GET:
        q= request.GET['q']
        # records = RecModel.objects.filter(sender__icontains = q)
        multiple_q = Q(Q(sender__icontains = q) | Q(subject__icontains = q))
        records = RecModel.objects.filter(multiple_q)
    else:
        records = RecModel.objects.all()
    context = {'records': records}
    return render(request, 'records/mailslist.html', context)


# for deleting records chosen
def records_delete(request, id):
    record_to_delete = RecModel.objects.get(pk=id)
    record_to_delete.delete()

    return records_list(request)


        
# def search_view(request):
#     query = request.GET.get('q')
#     return RecModel.objects.filter(sender__icontains= query)
        
   