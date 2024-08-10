from django.shortcuts import render

from .models import Question

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    response = "Results for Question %s:"
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "You're looking at the results of Question %s:"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on Question %s:" % question_id)
