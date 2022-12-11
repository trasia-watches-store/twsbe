from django.shortcuts import render
import pkg_resources
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
import os
import boto3
import uuid
import asyncio
from .models import Watch, WatchesPicture, MyModel
from .serializers import *
from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
# image tester
# @api_view(['GET', 'POST'])
# def upload(request):
    # if request.method == 'POST':    
    #     # parser_classes = [MultiPartParser, FormParser]
    #     # photo_file = request.FILES.get('file')
    #     # print(photo_file)
    #     return Response(photo_file, status=status.HTTP_200_OK)

# class upload(viewsets.ModelViewSet):
#     serializer_class = ImageTestSerializer
#     parser_classes = [MultiPartParser, FormParser]

#     def upload(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.order_by('-title')
    serializer_class = MyModelSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'])
    def perform_create(self, serializer):
        serializer.save()
        return Response({'status': 'password set'})

##################################################################################
@api_view(['GET', 'POST'])
def watches_list(request):
    if request.method == 'GET':
        watches = Watch.objects.all()
        serializer = WatchSerializer(watches, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        photo_file = request.FILES.get('wimage', None)
        print(f'photo_file: {photo_file}')
        if photo_file:
            s3 = boto3.client('s3')
            print(f's3: {s3}')
            # build a unique filename keeping the image's original extension
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            print(f'key: {key}')
            try:
                bucket = os.environ['S3_BUCKET']
                print(f'bucket: {bucket}')
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                print(url)
                request.data['wimage'] = url
                print(f'request.data.wimage: {request.data["wimage"]}')
                serializer = WatchSerializer(data=request.data)
                print(request.data)
                if serializer.is_valid():
                    serializer.save()
                    dict = serializer.data
                    print(dict['pk'])
                    print(dict)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                print('An error occurred uploading file to S3')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer = WatchSerializer(data=request.data)
        # print(request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     dict = serializer.data
        #     print(dict['pk'])
        #     print(dict)

            # if photo_file:
            # s3 = boto3.client('s3')
            # print(f's3: {s3}')
            # # build a unique filename keeping the image's original extension
            # key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            # print(f'key: {key}')
            # try:
            #     bucket = os.environ['S3_BUCKET']
            #     print(f'bucket: {bucket}')
            #     s3.upload_fileobj(photo_file, bucket, key)
            #     url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            #     print(url)
        # WatchesPicture.objects.create(url=url, cat_id=cat_id)
            # url='https://s3.ap-southeast-2.amazonaws.com/watchespics/0ebd2b.jpeg'
            # print(f'url: {url}')
            # pic = WatchesPicture.objects.create(url=url, watch_id=dict['pk'])
            # print(f'pic: {pic}')
            # picSerializer = WatchesPictureSerializer(pic)
            # print(f'picSerializer.data: {picSerializer.data}')
            # if picSerializer.is_valid():
            #     picSerializer.save()
            #     return print(f'picSerializer: {picSerializer}')
            # else:
            #     return print('An error occurred uploading file to S3')
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def watches_detail(request, pk):
    try:
        watch = Watch.objects.get(pk=pk)
        print(f'watch.wimage: {watch.wimage}')
    except Watch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        photo_file = request.FILES.get('wimage', None)
        print(f'photo_file: {photo_file}')
        if photo_file:
            s3 = boto3.client('s3')
            print(f's3: {s3}')
            # build a unique filename keeping the image's original extension
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            print(f'key: {key}')
            try:
                bucket = os.environ['S3_BUCKET']
                print(f'bucket: {bucket}')
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                print(url)
                request.data['wimage'] = url
                print(f'request.data.wimage: {request.data["wimage"]}')
                serializer = WatchSerializer(watch, data=request.data, context={'request': request})
                print(f'request.data: {request.data}')
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            except:
                print('An error occurred uploading file to S3')
        print(request.data)
        print(f'request.data.wimage: {request.data["wimage"]}')
        serializer = WatchSerializer(watch, data=request.data, context={'request': request})
        print(f'request.data: {request.data}')
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
        photo_file = request.FILES.get('image', None)
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