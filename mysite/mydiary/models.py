from django.db import models

# Create your models here.
class service(models.Model):
	service_name=models.CharField(max_length=200,primary_key=True)
	service_type=models.IntegerField()
	definition=models.CharField(max_length=400)
	method=models.CharField(max_length=200,null=True)
	modifier=models.CharField(max_length=200,null=True)
	def __unicode__(self):
		return self.service_name+"|"+self.service_type+"|"+self.definition+"|"+self.method


