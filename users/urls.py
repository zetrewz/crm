from django.urls import path

from users.views import get_current_user

app_name = 'users'

urlpatterns = [
    path('get_current_user/', get_current_user, name='get_current_user'),
]
