from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView

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