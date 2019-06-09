#coding:utf-8
"""定义learning_logs的URL Patterns"""
from django.conf.urls import url
from . import views

urlpatterns = [
	#主页
	url(r'^$',views.index,name='index'),
	#实现所有的主题
	url(r'^topics/$',views.topics,name='topics'),
	#实现主题下某个标题
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
	#实现添加主题
	url(r'^new_topic/$',views.new_topic,name='new_topic'),
	#实现添加条目
	url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
	#实现编辑条目
	url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name="edit_entry")
]
