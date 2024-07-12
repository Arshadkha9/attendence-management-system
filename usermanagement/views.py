from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the index page of myapp.")

def detail(request, id):
    return HttpResponse(f"This is the detail view with id {id}.")
