from django.db import models

class speakers(models.Model):
	name = models.CharField(max_length = 50)
	topic = models.CharField(max_length = 70)
	descr = models.TextField()
	time = models.DateTimeField()
	
	def __str__(self):
		return self.name 
	
