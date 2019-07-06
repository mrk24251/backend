from django.db import models

class mohammad(models.Model):
	firstname=models.CharField(max_length=100)
	email =models.EmailField(max_length=500,blank=True)
	message = models.CharField(max_length=500, blank=True)
	create_at=models.DateTimeField(auto_now_add=True)
	
