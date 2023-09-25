from django.urls import path

from .views import add_robot

app_name = 'robots'

urlpatterns = [
    path('add_robot/', add_robot, name='add_robot'),
]
