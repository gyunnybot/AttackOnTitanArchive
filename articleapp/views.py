from django.contrib.auth.decorators import login_required
from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic.list import ListView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


# Create your views here.


@method_decorator(login_required, 'dispatch')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    # 클라이언트 본인의 아티클만 생성할 수 있도록 서버에서 관리
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


# @method_decorator(login_required, name='dispatch') # 다른 사용자의 아티클 열람에 로그인이 필요할까?
# @method_decorator(article_ownership_required, name='dispatch') # 사용자 정보 열람에 계정 일치가 필요할까?
class ArticleDetailView(DetailView, FormMixin): # FormMixin을 활용한 다중 상속
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_article = self.get_object()

        # 다음 게시물 (같은 프로젝트에서 pk가 큰 것 중 가장 작은)
        next_article = Article.objects.filter(
            project=current_article.project,
            pk__gt=current_article.pk
        ).order_by('pk').first()

        # 이전 게시물 (같은 프로젝트에서 pk가 작은 것 중 가장 큰)
        prev_article = Article.objects.filter(
            project=current_article.project,
            pk__lt=current_article.pk
        ).order_by('-pk').first()

        context['next_article'] = next_article
        context['prev_article'] = prev_article
        return context

@method_decorator(login_required, 'dispatch')
@method_decorator(article_ownership_required, 'dispatch')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, 'dispatch')
@method_decorator(article_ownership_required, 'dispatch')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 10