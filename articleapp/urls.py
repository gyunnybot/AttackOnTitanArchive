from django.urls import path
from django.views.generic.base import TemplateView

app_name = "articleapp"

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]