from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),

    path('create/', AccountCreateView.as_view(), name = 'create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail'), # detail.html에는 pk가 필요하다!
    path('update/<int:pk>', AccountUpdateView.as_view(), name = 'update'), # update.html에는 pk가 필요하다!
    path('delete/<int:pk>', AccountDeleteView.as_view(), name = 'delete'), # detail.html에는 pk가 필요하다!
]