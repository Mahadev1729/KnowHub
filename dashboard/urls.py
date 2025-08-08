from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('notes',views.note,name="notes")
]
