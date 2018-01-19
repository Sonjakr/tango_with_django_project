# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome Page <a href='/rango/about/'>Go to: About</a>")
def about(request):
    return HttpResponse("Rango says here is the about page <a href='/rango/'>Go to: Main</a>")

# Create your views here.
