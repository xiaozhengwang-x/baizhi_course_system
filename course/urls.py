from django.urls import path
from course import views

app_name='course'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('pythonBase/',views.pythonBase,name='pythonBase'),
    path('addArticle/',views.addArticle,name='addArticle'),
    path('addArticle_logic/',views.addArticle_logic,name='addArticle_logic'),
    path('addCourse/', views.addCourse, name='addCourse'),
    path('addCourse_logic/',views.addCourse_logic,name='addCourse_logic'),
    path('update/',views.update,name='update'),
    path('update_logic/', views.update_logic, name='update_logic'),
    path('delete_logic/', views.delete_logic, name='delete_logic'),
    path('get_category/', views.get_category, name='get_category'),
    path('order/', views.order, name='order'),

]