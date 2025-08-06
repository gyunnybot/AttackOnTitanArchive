from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from commentapp.forms import CommentForm

# Create your views here.

@method_decorator(login_required, 'dispatch')
@method_decorator(comment_ownership_required, 'dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk })


@method_decorator(login_required, 'dispatch')
@method_decorator(comment_ownership_required, 'dispatch')
class CommentUpdateView(UpdateView):
    model = Comment
    context_object_name = 'target_comment'
    form_class = CommentForm
    template_name = 'commentapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(login_required, 'dispatch')
@method_decorator(comment_ownership_required, 'dispatch')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk })