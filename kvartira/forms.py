from django import forms
from .models import Kvartira

class KvartiraForm(forms.ModelForm):
    class Meta:
        model = Kvartira
        fields = ['title', 'deck','locashion', 'price',  'image']