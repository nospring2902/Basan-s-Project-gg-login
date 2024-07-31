from django.urls import path
from .views import main,temp, homepage, CreateForm, UpdateForm, DeleteForm, register, basan, log_in, log_out, dashboard, viewtasks, auth_receiver

urlpatterns = [
    path('home', main),
    path('temp', temp),
    path('', homepage, name='homepage'),
    path('create-form', CreateForm, name='create-tasks'),
    path('view', viewtasks, name='view-tasks'),
    path('update-tasks/<str:pk>/', UpdateForm, name='update-tasks'),
    path('delete-task/<str:pk>/', DeleteForm, name='delete-tasks'),
    path('register', register, name='register'),
    path('basan', basan, name='basan'),
    path('login', log_in, name='log_in'),
    path('logout', log_out, name='log_out'),
    path('dashboard', dashboard, name='dashboard'), 
    path('auth-receiver',auth_receiver, name='auth_receiver'),
]
