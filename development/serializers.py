from rest_framework import serializers

from development.models import Project, Team, Sprint, Task
from users.serializers import UserSS


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamDetailSerializer(serializers.ModelSerializer):
    members = UserSS(many=True)

    class Meta:
        model = Team
        fields = '__all__'


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class SprintListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class SprintDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class SprintCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class SprintUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
