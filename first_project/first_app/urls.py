from django.urls import path, re_path
from django.conf.urls import include

from first_app import views

app_name= "first_app"
urlpatterns = [
    path('',views.index, name= 'index' ),
    path('form',views.form_name_view, name= 'form' ),
   
    
    path('users',views.users, name= 'users' ),
    path('login',views.user_login, name= 'user_login' ),
    path('registeration',views.register, name= 'registeration' ),
    
    # path('users',views.List_users, name= 'list_users' ) ,   

    


]