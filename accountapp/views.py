from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from articleapp.models import Article


# Create your views here.
class AccountCreateView(CreateView): #계정 생성 클래스. class based view
    model = User
    form_class = UserCreationForm  # 계정
    success_url = reverse_lazy('accountapp:login') # 계정 생성 성공 시 다시 연결될 경로
    template_name = 'accountapp/create.html'


@method_decorator(login_required, name='dispatch') # 다른 유저의 정보를 보는 것은 로그인이 필요하다고 판단
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # 127.0.0.1:8000/accounts/detail/5에서 5가 바로 target_user
    template_name = 'accountapp/detail.html'

    paginate_by = 25 # 게시물 페이지네이션 개수

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object()) # 현재 페이지에서 조회 중인 유저의 게시물 가져오기

        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class AccountUpdateView(PasswordChangeView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)  # 비밀번호 변경 후 로그아웃

        return response


@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:login')