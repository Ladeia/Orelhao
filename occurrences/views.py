#!/usr/bin/python
#!-*- conding: utf8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Abra a sua ocorrência")
