# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Section, Topic

# create a serializer class
class LearningSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Section
		fields = ('title_main', 'sub_title ','image')


class Desc_detailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Topic
		fields = ('desc_title', 'description', 'video_uri')


class Title_detailsSerializer(serializers.ModelSerializer):
	subtitle = serializers.SerializerMethodField()
	image=serializers.SerializerMethodField()
	class Meta:
		model = Section
		fields = ('title_main', 'subtitle','image')
	def get_image(self,obj):
		return obj.image.url



	def get_subtitle(self,obj):
		result = []
		subtitle = obj.sub_title.all()
		for data in subtitle:
			title_sub = data.title_sub
			details = data.details.all()
			res = Desc_detailsSerializer(details, many=True).data
			res = {"title_sub": title_sub, "res": res}
			result.append(res)

		return result










