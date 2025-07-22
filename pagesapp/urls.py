# pagesapp/urls.py
from django.urls import path
from .views import notice_view, partnership_view, about_view

app_name = 'pagesapp'

urlpatterns = [
    path('notice/', notice_view, name='notice'),
    path('partnership/', partnership_view, name='partnership'),
    path('about/', about_view, name='about'),
]
