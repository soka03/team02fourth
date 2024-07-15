from django.urls import path
from .views import init_db

app_name='board'

urlpatterns=[
    path('',init_db)
]