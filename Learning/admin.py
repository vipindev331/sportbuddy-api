# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# import the model Todo
from .models import Section_details
from .models import Chapter_details
from .models import Description_details,Games_Type,Images,PlatformAdmin

# create a class for the admin-model integration
class TodoAdmin1(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('desc_title','description','video_uri')
class TodoAdmin2(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('title_sub',)
class TodoAdmin3(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('title_main','game_type')


class TodoAdmin4(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ('game_type',)

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Description_details,TodoAdmin1)
admin.site.register(Chapter_details,TodoAdmin2)
admin.site.register(Section_details,TodoAdmin3)
admin.site.register(Games_Type,TodoAdmin4)
admin.site.register(Images)



