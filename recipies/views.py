from django.shortcuts import render
from django.http import HttpResponse, request

def index(request):
    return HttpResponse('<h1>Recipies</h1> <h2>Welcome tho this basic recipies website</h2>')