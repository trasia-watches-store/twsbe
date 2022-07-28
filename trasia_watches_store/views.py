from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import boto3
import uuid
from .models import Watch, WatchesPicture
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

@api_view(['PUT', 'DELETE'])
def watches_detail(request, pk):
    try:
        watch = Watch.objects.get(pk=pk)
    except Watch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = WatchSerializer(watch, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])

def pics_list(request):
    if request.method == 'GET':
        pics = WatchesPicture.objects.all()
        serializer = WatchesPictureSerializer(pics, context={'request': request}, many=True)
        return Response(serializer.data)
# def pics_list(request, cat_id):
    elif request.method == 'POST':
        # photo-file will be the "name" attribute on the <input>
        photo_file = request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            # build a unique filename keeping the image's original extension
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                # WatchesPicture.objects.create(url=url, cat_id=cat_id)
                pic = WatchesPicture.objects.create(url=url)
                serializer = WatchesPictureSerializer(pic)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            except:
                print('An error occurred uploading file to S3')
        # return Response(url, cat_id=cat_id)