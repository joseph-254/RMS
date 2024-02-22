from django.contrib import admin

from recApp.models import IncomingMail, OutGoingMail, BaseAttachments, FileMovement

admin.site.register(IncomingMail)
admin.site.register(OutGoingMail)
admin.site.register(BaseAttachments)
admin.site.register(FileMovement)