from django.forms import ModelForm, forms
from .models import DemoDatabase


class DemoForm(ModelForm):

    class Meta:
        model = DemoDatabase
        fields = ['username', 'password']
