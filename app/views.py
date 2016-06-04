from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from app.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import ProviderSerializer
import uuid,os
from elasticsearch import Elasticsearch

def index(request):
    return HttpResponse("hello world")
