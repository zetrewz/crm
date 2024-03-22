from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from development.exceptions import UnableToCreateSprint, SprintNotProvided, UnableToAddTask, TaskIsFinished, \
    TaskAlreadyInProgress, InvitationAlreadyExists, InvitationPermissionDenied
from development.models import Project, Team, Sprint, Task, Invitation
from development.serializers import ProjectCreateSerializer, ProjectListSerializer, TeamCreateSerializer, \
    TeamListSerializer, TeamUpdateSerializer, TeamDetailSerializer, SprintListSerializer, SprintCreateSerializer, \
    SprintDetailSerializer, SprintUpdateSerializer, TaskListSerializer, TaskDetailSerializer, TaskUpdateSerializer, \
    TaskCreateSerializer, InviteToTeamSerializer
from users.serializers import UserSerializer

User = get_user_model()


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer

    # def perform_create(self, serializer):
        # serializer.save(head=self.request.user)


class TeamCreateView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(lead=self.request.user)


class SprintCreateView(CreateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintCreateSerializer

    def perform_create(self, serializer):
        for sprint in Sprint.objects.filter(team=serializer.validated_data['team']):
            if not sprint.finished:
                raise UnableToCreateSprint
        serializer.save()


class AddTaskToSprintView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer

    def perform_update(self, serializer):
        try:
            task = self.get_object()
            if task.finished:
                raise TaskIsFinished
            if task.sprint:
                raise TaskAlreadyInProgress
            sprint = serializer.validated_data['sprint']
            if sprint.finished:
                raise UnableToAddTask
        except KeyError:
            raise SprintNotProvided
        serializer.save(sprint=sprint)


class InviteToTeam(CreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InviteToTeamSerializer

    def perform_create(self, serializer):
        team = serializer.validated_data['team']
        if self.request.user != team.lead:
            raise InvitationPermissionDenied
        user = serializer.validated_data['user']
        if Invitation.objects.filter(user=user, team=team).exists():
            raise InvitationAlreadyExists
        serializer.save()


class UserInvitations(ListAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InviteToTeamSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class JoinTeam(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        serializer.save(team=serializer.validated_data['team'])


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer


class TeamDetailView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer


class TeamUpdateView(UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamUpdateSerializer


class SprintListView(ListAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintListSerializer


class SprintDetailView(RetrieveAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintDetailSerializer


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
