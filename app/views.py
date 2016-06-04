from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from app.models import *
from elasticsearch import Elasticsearch

def index(request):
    return HttpResponse("hello world")
