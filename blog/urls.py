from django.urls import path
from .views import post_list, post_detail, post_by_tag, post_by_category

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='posts'),
    path('<int:id>', post_detail, name='post_detail'),
    path('tag=<slug:tag>', post_by_tag, name='post_by_tag'),
    path('category=<slug:category>', post_by_category, name='post_by_category'),
]