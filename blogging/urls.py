from django.urls import path
from blogging.views import BlogListView, DetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('posts/<int:pk>', DetailView.as_view(), name="blog_detail"),
]
