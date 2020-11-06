from . import views
from django.urls import path


urlpatterns = [

    path('publish/', views.publish, name='publish page'),
    # path('signup/signupdone/', views.success, name='account success'),

]