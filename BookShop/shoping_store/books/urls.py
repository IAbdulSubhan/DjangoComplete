from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home_page"),
    path('new/', newbook, name="newbook_page"),
    path('all/', books, name="books_page"),
]