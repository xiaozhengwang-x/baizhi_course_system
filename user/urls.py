from django.urls import path
from user import views

app_name='user'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('register_logic/', views.register_logic, name='register_logic'),
    path('login/',views.login,name='login'),
    path('login_logic/',views.login_logic,name='login_logic'),
    path('get_captcha/',views.get_captcha,name='get_captcha'),
    path('register_username/',views.register_username,name='register_username'),
    path('register_pwd/',views.register_pwd,name='register_pwd'),
    path('active/',views.active,name='active'),
    path('logout/',views.logout,name='logout'),




]