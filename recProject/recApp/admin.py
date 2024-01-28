from django.contrib import admin

from recApp.models import AttachmentCategory, IncomingAttachments, IncomingMail, OutGoingMail, OutgoingAttachments



# Register your models here.

admin.site.register(AttachmentCategory)
admin.site.register(IncomingMail)
admin.site.register(IncomingAttachments)
admin.site.register(OutGoingMail)
admin.site.register(OutgoingAttachments)