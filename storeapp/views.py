from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from storeapp.forms import StoreCreationForm
from storeapp.models import Store


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class StoreCreateView(CreateView):
    model = Store
    form_class = StoreCreationForm
    # 게시물 생성시 해당 게시물로 이동시켜 줄 것임
    template_name = 'storeapp/create.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('storeapp:detail', kwarg={'pk':self.object.pk})