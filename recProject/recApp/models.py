
from django.utils.translation import gettext_lazy as _
from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class BaseAttachments(models.Model):
    name = models.CharField(_("attachment name"), max_length=156, unique=True )
    category = models.CharField(_("attachment category"), max_length=156)
    ref_number = models.CharField(_("reference number"), max_length=156, unique=True)
    # attachment = models.FileField(_("file"), upload_to="files/")

    def __str__(self):
        return self.name

  

class BaseMailRecord(models.Model):
    sender = models.CharField(_("name of the sender"), max_length=156)
    ref_number = models.CharField(_("reference number"), max_length=156)
    description = models.CharField(_("description"), max_length = 156)

    class Meta:
        abstract = True


class IncomingMail(TrackingModel, BaseMailRecord):
    address_date = models.DateField(_("address date"), blank=True, null=True)
    remarks = models.TextField(_("remarks"), blank=True, null=True)
    file = models.ForeignKey(BaseAttachments, on_delete = models.CASCADE, to_field ='name')

    class Meta:
        verbose_name_plural = "Incoming Mails"
        ordering = ["-id"]


class OutGoingMail(TrackingModel, BaseMailRecord):
    mail_destination = models.CharField(_("receiver"), max_length=156)
    collected_by = models.CharField(_("collected by"), max_length=156)
    date_of_collection = models.DateField(_("date of collection"))


class FileMovement(models.Model):
    file_name   = models.ForeignKey(BaseAttachments, on_delete = models.CASCADE, related_name='file name +', to_field ='name')
    file_number = models.ForeignKey(BaseAttachments, on_delete = models.CASCADE, related_name='file Ref. Number +', to_field ='ref_number')
    last_folio  = models.CharField(max_length=156)
    collected_by= models.CharField(max_length=156)
    destination_office = models.CharField(max_length=156)
    date_of_collection = models.DateField(_("date of collection"))
    remarks = models.CharField(max_length = 156)