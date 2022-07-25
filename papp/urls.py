from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('add-note/', views.add_note),
    path('delete-note/', views.DeleteNote),
    path('create-user/', views.CreateUser),
    path('create-profile/', views.create_profile),
    path('save-generated-password/', views.save_generated_password),
    path('download-template/<str:name>/', views.download_template),
    path('get-available-templates/', views.retrieve_all_templates),
    # path('logout/', auth_views.logout, name='logout'),
]