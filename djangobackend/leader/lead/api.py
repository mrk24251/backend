from lead.models import mohammad
from rest_framework import viewsets,permissions
from .serializer import mohammadserial

class mohammadset(viewsets.ModelViewSet):
	queryset = mohammad.objects.all()
	permission_classes =[
		permissions.AllowAny
	]
	serializer_class = mohammadserial
	