from rest_framework import serializers

from .models import Project, Task, Risk


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "space"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "name",
            "project",
            "type",
            "description",
            "assignee",
            "labels",
            "reporter",
            "status",
        ]


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = "__all__"
