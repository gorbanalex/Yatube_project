from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, groups):
    return HttpResponse('Страница постов групп')


# Create your views here.
