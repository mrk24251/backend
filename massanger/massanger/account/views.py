import django_filters
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions, generics, status
from rest_framework import filters
from rest_framework.response import Response

from account.serializer import Massangerserializer, Searchserializer
from massage.models import Massanger
from massage.serializers import UserSerializer, ProfileSerializer, SsSerializer
import django_filters.rest_framework
import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView

from account.serializer import ConversationListSerializer, MessageSerializer
from massage.models import ConversationList , Messages

class LoginViewSet(viewsets.ModelViewSet):

    queryset = Massanger.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Massangerserializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

class SearchhView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = Searchserializer
    def post(self, request, *args, **kwargs):
        r=HttpResponseRedirect('/search?search=%s'%(request.data['username']))
        return r

class ConversationListView(generics.ListCreateAPIView):
    queryset = ConversationList.objects.all()
    serializer_class = ConversationListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MessageView(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        request_serializer = MessageSerializer(data=self.request.data)
        if request_serializer.is_valid():
            l=request_serializer.data['receiver_id']
        # l=self.request.query_params.get(key='receiver_id')
        serializer.save(relatedUser=[self.request.user,User.objects.get(id=l)])
        # serializer.save(relatedUser=User.objects.get(id=3))
        # self.request.query_params.get('receiver_id')
# class MessageView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     # def get(self, request, format=None):
#     #     snippets = Snippet.objects.all()
#     #     serializer = SnippetSerializer(snippets, many=True)
#     #     return Response(serializer.data)
#
#     def post(self, request, format=None):
#         user_sender=self.request.user
#         user_reciever=User.objects.filter(id=7)
#         message=request.data
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#         message.relatedUser.add(user_reciever, user_sender)
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES
#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Messages.objects.all()
#     serializer_class = MessageSerializer
