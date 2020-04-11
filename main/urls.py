from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListAndCreateView.as_view(), name='main-page'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete-page'),
    path('finish/<int:pk>', views.finish_task, name='finish-page'),
    path('untick/<int:pk>', views.untick_finish, name='untick-page'),
    path('delete-all/', views.delete_all, name='delete-all-page'),
    path('delete-finished/', views.delete_completed_tasks, name='delete-finished-tasks'),
    path('untick-all/', views.untick_all, name='untick-all'),
]
