from django.urls import path
from . import views

urlpatterns = [
    path('translate/<str:lang>',views.translate)
]