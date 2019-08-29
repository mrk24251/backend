from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers
from rest_framework.utils import json


class Massanger(models.Model):
    username = models.CharField(max_length=200,blank=False)
    password = models.CharField(max_length=50,blank=False)
    first_name=models.CharField(max_length=100,blank=True, default="")
    last_name=models.CharField(max_length=100,blank=True, default="")
    city = models.CharField(max_length=100, blank=True, default="")
    bio = models.CharField(max_length=500, blank=True, default="")
    query = models.CharField(max_length=500, blank=False, default="")
    messages = models.CharField(max_length=500, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    token=models.CharField(max_length=500,default="")

class ConversationList(models.Model):
    first_name=models.CharField(max_length=100,blank=True, default="",null=True)
    last_name=models.CharField(max_length=100,blank=True, default="",null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='Messanger', on_delete=models.CASCADE,null=True)
    user_id=models.IntegerField(default=1)

    @property
    def latest_message(self):
        s=""
        ll=serializers.serialize("json", self.owner.Messages.filter(sender_id=self.user_id))
        struct = json.loads(ll)
        for i in struct:
            s=i
        return s

class Messages(models.Model):
    receiver_id=models.IntegerField()
    sender_id=models.IntegerField(default=2)
    text=models.CharField(max_length=500,blank=False)
    relatedUser = models.ManyToManyField(User,related_name='Messages')