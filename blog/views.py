from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
