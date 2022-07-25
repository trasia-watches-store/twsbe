from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Watch
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def watches_list(request):
    if request.method == 'GET':
        watches = Watch.objects.all()
        serializer = WatchSerializer(watches, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)