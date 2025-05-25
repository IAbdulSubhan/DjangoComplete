from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list" : latest_question_list }
    return render(request, 'polls/index.html', context)
#show page / detail page like polls/2/
def detail(request, question_id):
    try: 
        question = Question.objects.get(pk = question_id)
        context = {"question" : question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id) #Equilant to #return HttpResponse(f"You're voting on question {question_id}.")
