from django.urls import path
from .views import SpaceCreateView, SpaceListView, SpaceDetailView, SpaceEditView

urlpatterns = [
    path('create/', SpaceCreateView.as_view(), name='create_space'),
    path('list/', SpaceListView.as_view(), name='list_spaces'),
    path('<slug:slug>/', SpaceDetailView.as_view(), name='space_details'),
    path('edit/<slug:slug>/', SpaceEditView.as_view(), name='edit_space'),
]
