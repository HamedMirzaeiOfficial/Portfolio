from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='portfolio'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.ProjectDetailView.as_view(),
         name='project_detail'),

]
