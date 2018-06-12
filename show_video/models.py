from django.db import models

# Create your models here.

class Users(models.Model):
	username = models.CharField(max_length=50,primary_key=True)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

class Video(models.Model):
	v_id = models.AutoField(primary_key=True)
	#title = models.CharField(max_length=100)
	size = models.BigIntegerField()
	date = models.DateTimeField()
	file = models.FileField(upload_to='img/',default='unknown')

class User_Video(models.Model):
	username = models.ForeignKey(Users,on_delete=models.CASCADE)
	v_id = models.ForeignKey(Video,on_delete=models.CASCADE)
