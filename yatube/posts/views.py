from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse ("Это главная страница соц-сети для блорегов :)")


def group_posts(request, slug):
    return HttpResponse("А это страница с постами пользователей, которые отсортированы по группам.")
