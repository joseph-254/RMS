
from django.urls import path
from . import views

# app_name="records"

urlpatterns = [
    path('home/', views.home, name="home"),

    path('incoming/', views.records_form, name="insert"),
    path('incominglist/', views.records_list, name="view_mails"),
    path('<int:id>', views.records_form, name="update"),
    path('list/<int:id>', views.records_delete, name="delete"),

    path('outgoing/', views.outgoing_form, name="outgoing_form"),
    path('outgoinglist/', views.outgoing_list, name="outgoing_list"),
    path('outgoing/<int:id>', views.outgoing_form, name="outgoing_update"),
    path('outgoinglist/<int:id>', views.delete_outgoing, name="outgoing_delete"),
    
    path('files/', views.files_form, name="files_form"),
    path('fileslist/', views.files_list, name="view_files"),
    path('files/<int:id>', views.files_form, name="file_update"),
    path('fileslist/<int:id>', views.delete_file, name="file_delete"),
]