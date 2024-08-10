from django.shortcuts import render
from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # this gets all the questions sorted in descending order

    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)
    # renders the request (gotten from index function)
    # using the "polls/index.html" template
    # and uses context to fill it out, after which
    # the render will be returned!

def details(request, question_id):
    response = "Results for Question %s:"
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist!!!")
    return render(request, "polls/detail.html", {"question": question})

    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "You're looking at the results of Question %s:"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on Question %s:" % question_id)
