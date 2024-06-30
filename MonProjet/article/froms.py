from django import forms
from . models import Articles

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'description', 'image', 'price', 'actif','slug']