# # from typing import Any
# # from django.db import models

# #--------------------incoming mails model--------------------#

# # class FilesModel(models.Model):
# #     file_name = models.CharField(max_length= 255, unique=True)
# #     file_category = models.CharField(max_length= 255)
# #     file_ref_number =  models.CharField(max_length= 255)


# #     def __str__(self):
# #         return self.file_name

# # class RecModel(models.Model):
# #     register_date = models.DateField()
# #     sender = models.CharField(max_length = 255)
# #     ref_number = models.CharField(max_length = 255)
# #     subject = models.CharField(max_length = 255)
# #     address_date = models.DateField()
# #     remarks = models.CharField(max_length = 255)
# #     file_to = models.ForeignKey(FilesModel, on_delete = models.CASCADE, to_field='file_name')


# #--------------------outgoing mails model--------------------#
  
# # class OutgoingModel(models.Model):
# #     register_date = models.DateField()
# #     mail_sender = models.CharField(max_length = 255)
# #     mail_receiver = models.CharField(max_length = 255)
# #     ref_number = models.CharField(max_length = 255)
# #     subject = models.CharField(max_length = 255)
# #     collected_by = models.CharField(max_length = 255)
# #     collecting_date = models.DateField()
    




# from django.utils.translation import gettext_lazy as _
# from django.db import models
# from django.urls import reverse

# class TrackingModel(models.Model):
#     created_at = models.DateTimeField(_("created at"), auto_now_add=True)
#     updated_at = models.DateTimeField(_("updated at"), auto_now=True)

#     class Meta:
#         abstract = True


# class AttachmentCategory(TrackingModel):
#     category = models.CharField(_("attachment category"), max_length=156, unique=True)

#     def get_absolute_url(self):
#         return reverse("records:details",kwargs={"id":self.id})

#     def _str_(self):
#         return str(self.category) 

# class BaseAttachments(models.Model):
#     name = models.CharField(_("attachment name"), max_length=156)
#     category = models.ForeignKey(AttachmentCategory, on_delete=models.PROTECT)
#     ref_number = models.CharField(_("reference number"), max_length=156, unique=True)
#     attachment = models.FileField(_("file"), upload_to="files/")

#     class Meta:
#         abstract = True


# class BaseMailRecord(models.Model):
#     sender = models.CharField(_("name of the sender"), max_length=156)
#     ref_number = models.CharField(_("reference number"), max_length=156)
#     description = models.TextField(_("description"), null=True, blank=True)

#     class Meta:
#         abstract = True


# class IncomingMail(TrackingModel, BaseMailRecord):
#     address_date = models.DateField(_("address date"), blank=True, null=True)
#     remarks = models.TextField(_("remarks"), blank=True, null=True)

#     class Meta:
#         verbose_name_plural = "Incoming Mails"
#         ordering = ["-id"]


# class IncomingAttachments(TrackingModel, BaseAttachments):
#     """Incoming Mails Attachments"""
#     incoming_mail=models.ForeignKey(IncomingMail,on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "Incoming Attachments"
#         ordering = ["-id"]


# class OutGoingMail(TrackingModel, BaseMailRecord):
#     collected_by = models.CharField(_("collected by"), max_length=156)
#     date_of_collection = models.DateField(_("date of collection"))


# class OutgoingAttachments(TrackingModel, BaseAttachments):
#     """Incoming Mails Attachments"""
#     outgoing_mail=models.ForeignKey(OutGoingMail,on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "Outgoing Attachments"
#         ordering = ["-id"]

