from django.urls import path

from subscriptionapp.views import SubscriptionView

app_name = 'subscriptionapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe')
]