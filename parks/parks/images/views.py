from django.shortcuts import render
from . import models , serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parks.users import models as user_models

class Image(APIView):   # username 이 username 인 유저의 image 모두 불러오기

    def get(self , request , format=None):
        
        images = models.Image.objects.all()      

        if images is not None:

            serializer = serializers.ImageSerializer(images , many = True)
            
            return Response(data = serializer.data ,status = status.HTTP_200_OK)

        else :

            return Response(status = status.HTTP_404_NOT_FOUND)

class CreateImage(APIView):

    def post(self , request , format=None):

        user = request.user

        serializer = serializers.CreateImageSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data = serializer.data , status=status.HTTP_201_CREATED)

        else :

            return Response(data = serializer.errors , status=status.HTTP_400_BAD_REQUEST)
