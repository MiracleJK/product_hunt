from . import views
from django.urls import path


urlpatterns = [

    path('publish/', views.publish, name='publish page'),
    path('<int:product_id>/', views.product_detail, name='product detail'),
]