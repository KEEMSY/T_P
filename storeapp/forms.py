from django.forms import ModelForm

from storeapp.models import Store


class StoreCreationForm(ModelForm):
    class Meta:
        model = Store
        fields = ['title', 'image', 'content'] #여기서 디비 데이터 그대로 폼을 구성해야함