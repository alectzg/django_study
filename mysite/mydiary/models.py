from django.db import models

# Create your models here.
class service(models.Model):
	ATTR_TYPE_CHOICE=((1,"class Type"),
					  (0,"module func"),)
	service_name=models.CharField(max_length=200,primary_key=True)
	service_type=models.IntegerField()
	method=models.CharField(max_length=200,null=True)
	module=models.CharField(max_length=2000,null=True)
	attrType=models.IntegerField(choices=ATTR_TYPE_CHOICE)
	modifier=models.CharField(max_length=200,null=True)
	
	def __unicode__(self):
		return self.service_name
	
	def getFields(self,fieldName):
		if hasattr(self,fieldName):
			return getattr(self,fieldName)
		else:
			return None



class serv_ext(models.Model):
	service=models.ForeignKey(service)
	seq=models.IntegerField(default=0)
	section=models.CharField(max_length=1000)
	
	def __unicode__(self):
		return self.service.service_name+" | "+self.section
