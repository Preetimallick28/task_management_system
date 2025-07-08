from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:pk>',views.details,name='details'),
    path('add/',views.add_task,name='add'),
    path('update/<int:pk>',views.update_task,name='update'),    
    path('confirm_del/<int:pk>',views.confirm_del,name='confirm_del'),    
    path('delete/<int:pk>',views.delete_,name='delete'),
    path('history',views.history,name='history'),
    path('restore_all',views.restore_all,name='restore_all'),
    path('restore_task/<int:pk>',views.restore_task,name='restore_task'),
    path('clear_all',views.clear_all,name='clear_all'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('completed/<int:pk>',views.completed,name='completed'),
    path('complete_task',views.complete_task,name='complete_task'),


]
