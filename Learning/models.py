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

class Description_details(models.Model):
	desc_title=models.CharField(max_length=150)
	description=models.CharField(max_length=2050)
	video_uri=models.CharField(max_length=150)
	def __unicode__(self):
		return 'desc_title : %s' % self.desc_title


class Chapter_details(models.Model):
	title_sub=models.CharField(max_length=150)
	details = models.ManyToManyField(Description_details)

	def __unicode__(self):
		return 'Title : %s' % self.title_sub

class Images(models.Model):
	image=models.ImageField(upload_to='images',null=True)  
	name=models.CharField(max_length=150)
	def __unicode__(self):
		return 'Name : %s' % self.name

class Games_Type(models.Model):
	game_type=models.CharField(max_length=150)
	slideimages=models.ManyToManyField(Images, related_name='slideimage')
	splashImg=models.ForeignKey(Images, related_name='splashimg',on_delete=models.CASCADE)
	def __unicode__(self):
		return 'Name : %s' % self.game_type



class Section_details(models.Model):
	title_main=models.CharField(max_length=150)
	sub_title = models.ManyToManyField(Chapter_details)
	image = models.ImageField(upload_to='images',null=True)  
	game_type=models.ForeignKey(Games_Type,on_delete=models.CASCADE)
	

