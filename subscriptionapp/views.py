from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic import RedirectView, ListView
from django.utils.decorators import method_decorator

from articleapp.models import Article
from projectapp.models import Project
from subscriptionapp.models import Subscription
from django.core.paginator import Paginator


# Create your views here.


@method_decorator(login_required, 'dispatch')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})


    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) # project를 찾고, 없다면 404
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project) # {user, project} 쌍에 맞는 구독 정보

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class SubscriptionListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'subscriptionapp/list.html'
    paginate_by = 10

    def get_queryset(self):
        subscriptions = Subscription.objects.filter(user=self.request.user).values_list('project', flat=True)
        return Project.objects.filter(pk__in=subscriptions)