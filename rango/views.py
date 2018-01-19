# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake"}
    return render(request,'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page <a href='/rango/'>Go to: Main</a>")

# Create your views here.