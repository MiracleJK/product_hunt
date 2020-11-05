from . import views
from django.urls import path


urlpatterns = [

    path('signup/', views.signup, name='sign up page'),
    path('signup/signupdone/', views.success, name='account success'),

]