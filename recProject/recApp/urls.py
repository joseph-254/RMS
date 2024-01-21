
from django.urls import path
from . import views

urlpatterns = [
    path('', views.records_form, name="insert"),
    path('list/', views.records_list, name="view_mails"),
    path('<int:id>', views.records_form, name="update"),
    path('list/<int:id>', views.records_delete, name="delete"),
    path('outgoing/', views.outgoing_form, name="outgoing_form"),
    path('outgoinglist/', views.outgoing_list, name="outgoing_list"),
    path('outgoing/<int:id>', views.outgoing_form, name="outgoing_update"),
    path('outgoinglist/<int:id>', views.delete_outgoing, name="outgoing_delete")
]