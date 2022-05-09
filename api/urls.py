from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('posts/', views.PostList.as_view()),
#     path('posts/<int:pk>/', views.PostDetail.as_view()),
#     path('categories/', views.CategoryList.as_view()),
#     path('category/<int:pk>/', views.CategoryDetail.as_view())
#
# ]


""" using  routers, because we have a lot of duplicate code in views and than change it to viewset """

router = SimpleRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('category', views.CategoryViewSet, basename='categories')
router.register('projects', views.ProjectViewSet, basename='projects')
router.register('category_projects', views.CategoryProjectViewSet, basename='category_projects')
urlpatterns = router.urls
