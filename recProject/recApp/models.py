from typing import Any
from django.db import models

#--------------------incoming mails model--------------------#

class FilesModel(models.Model):
    file_category = models.CharField(max_length= 255)
    file_name = models.CharField(max_length= 255, unique=True)
    file_ref_number =  models.CharField(max_length= 255)


    def __str__(self):
        return self.file

class RecModel(models.Model):
    register_date = models.DateField()
    sender = models.CharField(max_length = 255)
    ref_number = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    address_date = models.DateField()
    remarks = models.CharField(max_length = 255)
    file_to = models.ForeignKey(FilesModel, on_delete = models.CASCADE, to_field='file_name')


# class SearchModel(models.Model):
#     search = models.CharField(max_length = 255)
    


#--------------------outgoing mails model--------------------#
    

class OutgoingModel(models.Model):
    register_date = models.DateField()
    mail_sender = models.CharField(max_length = 255)
    mail_receiver = models.CharField(max_length = 255)
    ref_number = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    collected_by = models.CharField(max_length = 255)
    collecting_date = models.DateField()
    


