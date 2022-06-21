from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('questions/', views.questions, name="questions"),
    path('themes/', views.themes, name="themes"),
    path('man_themes/', views.manage_themes, name="create_themes"),
    path('man_themes/<str:pk>', views.manage_themes, name="update_themes"),
    path('del_themes/<str:pk>', views.delete_themes, name="delete_themes"),    
    path('tags/', views.tags, name="tags"),
    path('man_tags/', views.manage_tags, name="create_tags"),
    path('man_tags/<str:pk>', views.manage_tags, name="update_tags"),
    path('del_tags/<str:pk>', views.delete_tags, name="delete_tags"),
]