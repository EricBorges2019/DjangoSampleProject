from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from django.db.models import F
from django.urls import reverse


from .models import Question, Choice

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of Question %s:"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,            #given the request...
            "polls/detail.html",#render out this template using the below JSON.
            {
                "question": question,
                "error_message": "You didn't select a choice!",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
