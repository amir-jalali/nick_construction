from rest_framework import serializers
from .models import Project, ProjectProgress, ProjectMedia, ProjectNote


class ProjectMediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectMedia
        fields = ('id', 'image', 'caption', 'created_at')

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProjectNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectNote
        fields = ('id', 'text', 'created_at')


class ProjectProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgress
        fields = ('id', 'date', 'predicted', 'actual')


class ProjectSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()
    notes = ProjectNoteSerializer(many=True, read_only=True)
    progress = ProjectProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'location', 'area', 'price_per_meter',
                  'total_capital', 'predicted_profit', 'start_date',
                  'predicted_end_date', 'description', 'is_active',
                  'media', 'notes', 'progress', 'created_at')

    def get_media(self, obj):
        request = self.context.get('request')
        return ProjectMediaSerializer(
            obj.media.all(),
            many=True,
            context={'request': request}
        ).data

    class Meta:
        model = Project
        fields = ('id', 'name', 'location', 'area', 'price_per_meter',
                  'total_capital', 'predicted_profit', 'start_date',
                  'predicted_end_date', 'description', 'is_active',
                  'media', 'notes', 'progress', 'created_at')