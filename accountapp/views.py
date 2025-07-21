from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld
from articleapp.models import Article


# Create your views here.

@login_required
def hello_world(request): # function based view

    if request.method == "POST": # post

        temp = request.POST.get('hello_world_input') # 데이터 입력

        new_hello_world = HelloWorld() # 데이터베이스에 호환 가능한 HelloWorld 타입 변수 선언
        new_hello_world.text = temp # 입력받은 데이터를 DB에 호환되도록 가공?
        new_hello_world.save() # save

        return HttpResponseRedirect(reverse('accountapp:hello_world')) # 저장 완료 후 home으로 리다이렉트
    else: # get
        hello_world_list = HelloWorld.objects.all() # HelloWorld 모델에 저장된 모든 데이터를 불러옵니다
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) # 렌더링. 모든 데이터를 보여줍니다


class AccountCreateView(CreateView): #계정 생성 클래스. class based view
    model = User
    form_class = UserCreationForm  # 계정
    success_url = reverse_lazy('accountapp:hello_world') # 계정 생성 성공 시 다시 연결될 경로
    template_name = 'accountapp/create.html'


# @method_decorator(login_required, name='dispatch') # 사용자 정보 열람에 로그인이 필요할까?
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User # django에서 사용하는 기본 유저 테이블 클래스. 머신러닝 모델 선택하는 것과 비슷한 맥락
    context_object_name = 'target_user' # 127.0.0.1:8000/accounts/detail/5에서 5가 바로 target_user!
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())

        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)



@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class AccountUpdateView(PasswordChangeView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:hello_world')


@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:login')