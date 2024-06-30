from django import forms
from . models import Articles

class ArticlesForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'la description ici',
            }
        ))
    class Meta:
        model = Articles
        fields = ['name', 'description', 'image', 'price', 'actif','slug']