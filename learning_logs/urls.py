"""Defines the URL pattern for the learning logs"""

from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # topics page
    path('topics/', views.topics, name='topics'),
    # a single topic page with the associated entries
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # create new topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    # create a new entry page
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # edit a previous entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
