from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='organizations'),
    path('<int:organization_id>', views.organization, name='organization'),
   
]