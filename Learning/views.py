# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.decorators import list_route

# import the TodoSerializer from the serializer file
from .serializers import LearningSerializer, Title_detailsSerializer
from .models import Sport
# import the Todo model from the models file
from .models import Section
# create a class for the Todo model viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view,action

class LearningView(viewsets.ReadOnlyModelViewSet):



	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = LearningSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = Section.objects.all()

	# @api_view()
	@action(detail=False)
	def getDetails(self, request):
		todo_id = request.GET.get('id')
		print("todo_id",todo_id)
		todo=Section.objects.all()		
		message = 'Success'

		return Response({"message": message,"data": LearningSerializer(todo).data})

	# @api_view()
	@action(detail=False)
	def getChapter(self, request):
		data = Section.objects.filter(game_name__id=request.GET.get('id'))
		result = Title_detailsSerializer(data,many=True).data
		splash= ""
		imgs=[]
		for datas in data:
			slideimg=datas.game_name.slide_images.all()
			splash=datas.game_name.splashImg.image.url
			for img in slideimg:
				print ("----img.image----", img.image.url)
				imgs.append(img.image.url)

			
		

		return Response({"result": result,"splash_img":splash,"slide_img":imgs})



