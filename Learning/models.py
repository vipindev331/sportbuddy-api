# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.contrib import  admin
from django.db import models

# Create your models here.

# class Todo(models.Model):
# 	id=models.IntegerField(primary_key=True)
# 	title=models.CharField(max_length=150)
# 	description=models.CharField(max_length=25000)
# 	videouri=models.CharField(max_length=200,default='')
class PlatformAdmin(admin.ModelAdmin):
    pass

class Topic(models.Model):
	desc_title=models.CharField(max_length=150)
	description=models.CharField(max_length=2050)
	video_uri=models.CharField(max_length=150)
	def __str__(self):
		return 'Desc Title : %s' % self.desc_title


class Chapter(models.Model):
	title_sub=models.CharField(max_length=150)
	details = models.ManyToManyField(Topic)

	def __str__(self):
		return 'Title : %s' % self.title_sub

class Image(models.Model):
	image=models.ImageField(upload_to='images',null=True)  
	name=models.CharField(max_length=150)
	def __str__(self):
		return 'Name : %s' % self.name

class Sport(models.Model):
	game_name=models.CharField(max_length=150)
	slide_images=models.ManyToManyField(Image, related_name='slide_image')
	splashImg=models.ForeignKey(Image, related_name='splashimg',on_delete=models.CASCADE)
	def __str__(self):
		return 'Name : %s' % self.game_name



class Section(models.Model):
	title_main=models.CharField(max_length=150)
	sub_title = models.ManyToManyField(Chapter)
	image = models.ImageField(upload_to='images',null=True)  
	game_name=models.ForeignKey(Sport,on_delete=models.CASCADE)
	

