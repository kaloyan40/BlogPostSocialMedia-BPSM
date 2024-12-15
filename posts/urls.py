from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView, PostDetailView, PostEditView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('edit/<slug:slug>/', PostEditView.as_view(), name='edit_post'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_details'),
]
