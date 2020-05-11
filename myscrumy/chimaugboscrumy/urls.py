#Django
from django.urls import path

#local
from . import views

urlpatterns = [
    path('', views.get_grading_parameters, name='get_grading_parameters'),
]

