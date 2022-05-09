from rest_framework import serializers
from blog.models import Category, Post
from project.models import Project, CategoryProject


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'created_on', 'last_modified')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'image', 'body',
                  'created_on', 'last_modified',
                  'category', 'active')


class CategoryProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProject
        fields = ('name', 'created_on', 'last_modified')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'slug', 'image', 'body',
                  'created_on', 'last_modified',
                  'category', 'active')


