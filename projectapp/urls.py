from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView, ProjectDeleteView, ProjectUpdateView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),
    path('list/', ProjectListView.as_view(), name='list'),
]