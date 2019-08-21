from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView

from account.serializer import Massangerserializer
from methods.permission import IsOwnerOrReadOnly
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer


#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": LoginSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#Profile User API
class ProfileAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProfileSerializer
    def post(self,request,*args):
        serializer = ProfileSerializer(request.user,data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": Massangerserializer(user).data
        })
