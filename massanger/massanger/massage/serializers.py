from django.contrib.auth.models import User
from rest_framework import serializers

from account.serializer import ConversationListSerializer, MessageSerializer
from .models import Massanger
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
	Messanger = ConversationListSerializer(many=True, read_only=True)
	Messages= MessageSerializer(many=True,read_only=True)
	class Meta:
		model = User
		fields = ['id', 'username','first_name','last_name','Messanger','Messages']

#Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = Massanger
		fields = ('username','password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'],password=validated_data['password'])
		user.save()
		return user

#login serializer
class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = Massanger
		fields = ('username','password','id')
		extra_kwargs = {'password': {'write_only': True}}
		extra_kwargs = {'id': {'read_only': True}}

	def validate(self, data):
		user = authenticate(**data)
		if user is not None:
			return user
		raise serializers.ValidationError("Incorrect Credential")

#Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Massanger
		fields = ('id','first_name','last_name' ,'city', 'bio','token')

	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.save()
		return instance

class SsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Massanger
		fields = ('id','messages')

	def update(self, instance, validated_data):
		instance.messages = validated_data.get('messages', instance.messages)
		instance.save()
		return instance


#Create massages Serializer
class CreateMassageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Massanger
		fields = ('id', 'massages')

	def update(self, instance, validated_data):
		instance.messages = validated_data.get('messages', instance.bio)
		return instance