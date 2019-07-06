from rest_framework import serializers
from lead.models import mohammad

class mohammadserial(serializers.ModelSerializer):
	class Meta:
		model = mohammad
		fields ='__all__'