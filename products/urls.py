from . import views
from django.urls import path


urlpatterns = [

    path('publish/', views.publish, name='publish page'),
]