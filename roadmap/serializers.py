from django.contrib.auth.models import User
from rest_framework import serializers

from roadmap.models import Project, Roadmap, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('name', 'explanation')


class RoadSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True, source='publications')

    class Meta:
        model = Roadmap
        fields = ('name', 'steps')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProjectSerializer(serializers.ModelSerializer):
    roadmap = RoadSerializer(many=False, read_only=True)
    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'roadmap', 'owner')
