# class that will take the model and convert it into serializer

from rest_framework import serializers
from .models import BlogPost 

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']
        # fields = '__all__'

        # class Meta:
