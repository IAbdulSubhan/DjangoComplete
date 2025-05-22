from django.urls import path
from . import views #access to all view


urlpatterns = [
    path('members/', views.members, name="members") #name is like we do as in rails like memebers_path etc
]


