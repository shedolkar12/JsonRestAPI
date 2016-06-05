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
        s = ProviderSerializer(prov, many=True)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        return Response(s.data)
    elif request.method=='DELETE':
        prov.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        data = request.data
        instance = prov[0]
        for attr, value in data.iteritems():
            print attr, value,prov
            setattr(instance, attr, value)
        instance.save()
        return Response(s.data)

@api_view(['GET', 'POST'])
def service_area(request, id):
    try:
        prov = Provider.objects.filter(provider_id=id)
        s = ProviderSerializer(prov, many=True)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        query = {
            "query": {
                "match": {
                    "provider_id": id
                    }
                }
            }
        data = []
        try:
            result = es.search(index='tt', body=query)
            for d in result['hits']['hits']:
                data.append(d['_source'])
        except:
            pass
        return Response({'data':data})
    elif request.method=='POST':
        data = request.data
        for attr in ['area_name', 'price', 'area']:
            if attr not in data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                if attr=='price':
                    try:
                        data[attr] = float(attr)
                    except ValueError:
                        return Response(status=status.HTTP_404_NOT_FOUND)
                elif attr=='area':
                    for point in data['area']:
                        i=0
                        try:
                            point[0] = float(point[0])
                            point[1] = float(point[1])
                            data['area'][i] = point
                            i+=1
                        except ValueError:
                            return Response(status=status.HTTP_404_NOT_FOUND)
            polygon_id = uuid.uuid4().hex
            final_data = {
            "provider_id": id,
            "area_id": polygon_id,
            "area_name": data["area_name"],
            "price": data["price"],
            "location": {
                    "type": "polygon",
                    "coordinates": [ data["area"] ]
                    },
            }
            print final_data
            es.index(index="tt", doc_type="list", id=polygon_id, body=final_data)

            return Response(final_data)
