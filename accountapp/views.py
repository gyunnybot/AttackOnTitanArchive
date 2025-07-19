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

from accountapp.authenticate import user_is_owner
from accountapp.models import HelloWorld


# Create your views here.

@login_required
def hello_world(request): # function based view

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all() # reverse = 함수, reverse_lazy = 클래스
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView): #계정 생성 클래스. class based view
    model = User  # pk 값으로 DB에서 가져오는 객체 = target_user
    form_class = UserCreationForm  # 계정
    success_url = reverse_lazy('accountapp:hello_world') # 계정 생성 성공 시 다시 연결될 경로
    template_name = 'accountapp/create.html'


# @method_decorator(login_required, name='dispatch') # 사용자 정보 열람에는 로그인이 필요한가?
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_owner, name='dispatch')
class AccountUpdateView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:hello_world')

@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_owner, name='dispatch')
class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:login')