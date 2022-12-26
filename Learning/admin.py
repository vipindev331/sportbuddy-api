# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# import the model Todo
from .models import Section
from .models import Chapter
from .models import Topic,Sport,Image,PlatformAdmin

# create a class for the admin-model integration
class TodoAdmin1(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('desc_title','description','video_uri')
class TodoAdmin2(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('title_sub',)
class TodoAdmin3(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('title_main','game_name')


class TodoAdmin4(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('game_name',)

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Topic,TodoAdmin1)
admin.site.register(Chapter,TodoAdmin2)
admin.site.register(Section,TodoAdmin3)
admin.site.register(Sport,TodoAdmin4)
admin.site.register(Image)



