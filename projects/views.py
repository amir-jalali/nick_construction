from rest_framework import generics, permissions
from .models import Project, ProjectProgress, ProjectMedia, ProjectNote
from .serializers import ProjectSerializer, ProjectProgressSerializer, ProjectMediaSerializer, ProjectNoteSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ProjectProgressListView(generics.ListAPIView):
    serializer_class = ProjectProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProjectProgress.objects.filter(project_id=self.kwargs['pk'])


class ProjectMediaListView(generics.ListAPIView):
    serializer_class = ProjectMediaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProjectMedia.objects.filter(project_id=self.kwargs['pk'])


class ProjectNoteListView(generics.ListAPIView):
    serializer_class = ProjectNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProjectNote.objects.filter(project_id=self.kwargs['pk'])