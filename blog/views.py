from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView


class HomePageView(TemplateView):
    template_name = 'homepage.html'
