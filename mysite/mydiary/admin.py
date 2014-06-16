from django.contrib import admin

# Register your models here.

from mydiary.models import service,serv_ext

class service_admin(admin.ModelAdmin):
	#fields=["service_name","service_type","definition","method"]
	
	fieldsets = [
	 (None,{"fields":["service_name"]}),
	 ("Service Detail",{"fields":["service_type","definition","method","modifier"]}),
	]
	
	list_display=("service_name","service_type","definition","method","modifier")

class serv_ext_admin(admin.ModelAdmin):
	fields=["service","seq","section"]
	list_display=("service","seq","section")

admin.site.register(service,service_admin)
admin.site.register(serv_ext,serv_ext_admin)
