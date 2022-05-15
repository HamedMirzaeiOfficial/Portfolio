from blog.models import Post, Category
from project.models import Project, CategoryProject
from api.serializers import PostSerializer, CategorySerializer, ProjectSerializer, CategoryProjectSerializer
from rest_framework import generics, viewsets

""" using viewsets, because we have a lot of duplicate code  """


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CategoryProjectViewSet(viewsets.ModelViewSet):
    queryset = CategoryProject.objects.all()
    serializer_class = CategoryProjectSerializer



