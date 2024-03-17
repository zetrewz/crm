from django.urls import path

from development.views import ProjectListView, ProjectCreateView, TeamListView, TeamCreateView, TeamUpdateView, \
    TeamDetailView, SprintListView, SprintCreateView, SprintDetailView, SprintUpdateView, TaskListView, TaskDetailView, \
    TaskCreateView, TaskUpdateView

app_name = 'development'

urlpatterns = [
    path('project/list/', ProjectListView.as_view(), name='project-list'),
    path('project/create/', ProjectCreateView.as_view(), name='project-create'),

    path('team/list/', TeamListView.as_view(), name='team-list'),
    path('team/detail/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('team/create/', TeamCreateView.as_view(), name='team-create'),
    path('team/update/<int:pk>/', TeamUpdateView.as_view(), name='team-update'),

    path('sprint/list/', SprintListView.as_view(), name='sprint-list'),
    path('sprint/detail/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),
    path('sprint/create/', SprintCreateView.as_view(), name='sprint-create'),
    path('sprint/update/<int:pk>/', SprintUpdateView.as_view(), name='sprint-update'),

    path('task/list/', TaskListView.as_view(), name='task-list'),
    path('task/detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
]
