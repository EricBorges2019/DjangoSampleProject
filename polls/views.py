from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request, question_id):
    response = "Results for Question %s:"
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "You're looking at the results of Question %s:"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on Question %s:" % question_id)
