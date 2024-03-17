from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from development.exceptions import UnableToCreateSprint
from development.models import Project, Team, Sprint, Task
from development.serializers import ProjectCreateSerializer, ProjectListSerializer, TeamCreateSerializer, \
    TeamListSerializer, TeamUpdateSerializer, TeamDetailSerializer, SprintListSerializer, SprintCreateSerializer, \
    SprintDetailSerializer, SprintUpdateSerializer, TaskListSerializer, TaskDetailSerializer, TaskUpdateSerializer, \
    TaskCreateSerializer


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer

    def perform_create(self, serializer):
        serializer.save(head=self.request.user)


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer


class TeamDetailView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer


class TeamCreateView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer

    def perform_create(self, serializer):
        serializer.save(lead=self.request.user)


class TeamUpdateView(UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamUpdateSerializer


class SprintListView(ListAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintListSerializer


class SprintDetailView(RetrieveAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintDetailSerializer


class SprintCreateView(CreateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintCreateSerializer

    def perform_create(self, serializer):
        for sprint in Sprint.objects.filter(team=serializer.validated_data['team']):
            if not sprint.finished:
                raise UnableToCreateSprint
        serializer.save()


class SprintUpdateView(UpdateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintUpdateSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
