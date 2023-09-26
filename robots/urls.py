from django.urls import path

from .views import add_robot, get_report

app_name = 'robots'

urlpatterns = [
    path('add_robot/', add_robot, name='add_robot'),
    path('weekly_report/', get_report, name='report'),
]
