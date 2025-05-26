from django.urls import path
from . import views

"""Namespacing URL names
Confusion template tag mein hota hai, URL mein nahi
Jab hum template ke andar likhte hain:

{% url 'detail' question.id %}
To Django ye check karta hai:

Is project mein koi URL hai jiska name='detail' hai?

Agar multiple apps (polls, blog, etc.) mein name='detail' ho, tab confusion hota hai.
"""

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/",views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/",views.ResultsView.as_view(), name="results"),
    #other than below all are class based view, but only below one using function based view
    path("<int:question_id>/vote/",views.vote, name="vote")
]
