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
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
