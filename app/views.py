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
    # print(request.GET.dict())
    # print(request.GET)
    # Dict = request.GET.dict()
    if request.method=='GET':
        provider=Provider.objects.all()
        s = ProviderSerializer(provider, many=True)
        return Response(s.data)

    elif request.method=='POST':
        provider_id = uuid.uuid4().hex
        data = request.data
        if 'provider_id' not in data:
            data['provider_id'] = provider_id

        serial = ProviderSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_info(request, id):

    try:
        prov = Provider.objects.filter(provider_id=id)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        s = ProviderSerializer(prov, many=True)
        return Response(s.data)
    elif request.method=='DELETE':
        prov.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # elif request.method=='PUT':

    return HttpResponse('hi')
