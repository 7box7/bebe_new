from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, "elevan_class/gen_info.html", context)
