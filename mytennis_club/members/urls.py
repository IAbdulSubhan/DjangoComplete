from django.urls import path
from . import views #access to all view


urlpatterns = [
    path('members/', views.members, name="members")
]


