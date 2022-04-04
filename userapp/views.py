import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from userapp.decorators import account_ownership_required
from userapp.forms import UserUpdateForm

has_ownership = [login_required, account_ownership_required]
#
# class tempView(View):
#     params = json.loads(request.body.decode('utf-8'))
#     id = params['id']
#     password = params['password']
#
#     result = User.objects.all()
#     # 쿼리셋은 for문을 통해 꺼내야함
#     result[0]['username']
#     # result = User.objects.values()
#     #valuse() : 단일객체(row)에 대해서만 가능
#     # result[0]['username']
#
#     result = User.objects.get(pk=1).valuse()
#
#     # 필터링을 해줄 때, 변수를 만들어서 딕셔너리로 만듬
#     user_name = result.username
#     user_nickname = result.nickname
#
#     user = {'user_name': user_name, 'user_nickname':user_nickname}
#     return  JsonResponse({"result": user}) #직렬화
#

class UserCreateView(CreateView):
    # def get(self,request):
    #     return render()
    #
    # def post(self,request):
    #     return render()

    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('userapp:login')
    template_name = 'userapp/create.html'



class UserDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'userapp/detail.html'



@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('userapp:detail')
    template_name = 'userapp/update.html'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class UserDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('userapp:login')
    template_name = 'userapp/delete.html'


def HomeView(request):
    return render(request, 'main.html')