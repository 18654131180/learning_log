from django.db import models
from django.contrib.auth.models import User #引用django的登录用户，这个是django默认的用户models


# Create your models here.
class Topic(models.Model):
	"""用户学习的主题"""
	text=models.CharField(max_length=200)
	date_added=models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User) #创建关联表与Django的登录User有外键关系
	def __str__(self):
		"""返回model的字符串表示"""
		return self.text

class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic=models.ForeignKey(Topic)
	text = models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "entries"

	def __str__(self):
		"""返回Model的字符串表示"""
		return self.text[:50] + "..."

