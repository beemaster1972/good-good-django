from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# здесь объявляйте функцию

def index(request):
    return HttpResponse('<h1>Достопримечательности Полевского</h1>')
def about(request):
    return HttpResponse("О сайте")
# Create your views here.
