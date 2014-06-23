from django.conf.urls import patterns,include,url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('',
	url(r'^index$','mydiary.views.index'),
	url(r'^searchService/(?P<serviceName>\w+)/$','mydiary.views.showService'),
	url(r'^callAjax/','mydiary.views.callAjax'),
	url(r'^displayMsg/$','mydiary.views.sendMsg'),
	url(r'^ajax_test/$','mydiary.views.testAjax'),
	url(r'^file/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_FILE["mydiary"]}),
)
