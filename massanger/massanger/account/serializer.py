from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from massage.models import Massanger
from massage.models import ConversationList , Messages

class Searchserializer(serializers.Serializer):
	username = serializers.CharField()

class Massangerserializer(serializers.ModelSerializer):
	class Meta:
		model = Massanger
		fields = '__all__'

class ConversationListSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConversationList
		fields = ['first_name', 'last_name', 'create_at','user_id']

# class RelateMessageUserSerializer(serializers.ModelSerializer):
#
# 	class Meta:
# 		model = User
# 		fields = ['Messages','username']
#
# class MessageSerializer(serializers.ModelSerializer):
#     relatedUser = RelateMessageUserSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Messages
#         fields= ['receiver_id','text','sender_id']
#
class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Messages
		fields = ['text','receiver_id','sender_id']