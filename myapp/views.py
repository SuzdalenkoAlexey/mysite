from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
import socket


def index(request):
    # with connections['default'].cursor() as cursor:
    #     cursor.execute("SELECT * FROM mi_tabla")
    mi_host_name = socket.gethostname()
    print(mi_host_name)

    return HttpResponse("Hello, world. You're at the index.")
