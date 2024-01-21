
from django.urls import path
from . import views

urlpatterns = [
    path('', views.records_form, name="insert"),
    path('<int:id>', views.records_form, name="update"),
    path('list/', views.records_list, name="view_mails"),
    path('list/<int:id>', views.records_delete, name="delete"),
    path('outgoing/', views.outgoing_form, name="outgoing_form"),
    path('outgoinglist/', views.outgoing_list, name="outgoing_list")
]