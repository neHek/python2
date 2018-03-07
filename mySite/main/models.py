from django.db import models

class Speakers(models.Model):
	name = models.CharField(max_length = 50)
	topic = models.CharField(max_length = 70)
	descr = models.TextField()
	time = models.DateTimeField()
	sect = models.ForeignKey('main.Section', on_delete=models.CASCADE, default = 1)
	
	def __str__(self):
		return self.name 
	
class Section(models.Model):
	sect = models.CharField(max_length = 2)
	
	def __str__(self):
		return self.sect 