from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectProgressListView,
    ProjectMediaListView,
    ProjectNoteListView
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/progress/', ProjectProgressListView.as_view(), name='project_progress'),
    path('<int:pk>/media/', ProjectMediaListView.as_view(), name='project_media'),
    path('<int:pk>/notes/', ProjectNoteListView.as_view(), name='project_notes'),
]