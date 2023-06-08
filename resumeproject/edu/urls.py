from django.urls import path
from . import views
urlpatterns=[
    path('skillset/', views.skillset, name='skill')
]