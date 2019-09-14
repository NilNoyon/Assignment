from http import client

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework_bulk.generics import ListBulkCreateAPIView

from taskapp.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import *
# Create your views here.


class CategoryAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request):
        snippet = Category.objects.all()
        print(snippet)
        serializer = CategorySerializer(snippet,many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = CategorySerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GameAPI(APIView):
    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request):
        snippet = Game.objects.all()
        print(snippet)
        serializer = GameListSerializer(snippet,many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = GameListSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)