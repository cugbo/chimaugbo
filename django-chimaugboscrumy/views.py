# Django
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Welcome to Django")
    return HttpResponse("This is a Scrum Application")