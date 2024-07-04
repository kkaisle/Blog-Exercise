from django.urls import path
from . import views

urlpatterns = [
    path("blogposts", views.BlogPostListView.as_view(), name="blogpost-list"),
]