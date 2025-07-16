from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from accountapp.models import HelloWorld


# Create your views here.

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
    model = User # 사용자 정보
    form_class = UserCreationForm  # 계정
    success_url = reverse_lazy('accountapp:hello_world') # 계정 생성 성공 시 다시 연결될 경로
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # 타인이 특정 사용자 페이지를 방문했을 때, 특정 사용자의 정보 표시
    template_name = 'accountapp/detail.html'


class AccountUpdateView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:hello_world') # 비밀번호 변경 후 hello_world로 리다이렉트


class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accountapp/delete.html'
    success_url = reverse_lazy('accountapp:login')  # 회원탈퇴 후 login으로 리다이렉트