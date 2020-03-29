from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListAndCreateView.as_view(), name='main-page'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete-page'),
]
