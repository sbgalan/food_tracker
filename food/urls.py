from django.conf.urls import url

from .views import * #imports from views.py

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_meal$', add_meal, name='add-meal'),
    url(r'^delete_meal/(?P<meal_id>\d+)$', delete_meal, name='delete-meal'),
    url(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
    url(r'^view_meal/(?P<meal_id>\d+)$', view_meal, name='view-meal'),
]
