from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
