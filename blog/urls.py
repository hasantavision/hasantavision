from django.urls import path
from .views import (BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView,
                    TagListView, SearchResultListView)


urlpatterns = [
    path("post/<uuid:pk>/delete", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<uuid:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new", BlogCreateView.as_view(), name="post_new"),
    path("<slug:slug>", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name='home'),
    path("search/", SearchResultListView.as_view(), name='search_result'),
    path("tag/", TagListView.as_view(), name='tag_result')
]
