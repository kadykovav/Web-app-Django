from django import forms

from .models import BlogPost


class Form(forms.Form):
    name = forms.CharField(max_length=255)


class PostForm(forms.ModelForm):
    slug = forms.SlugField(widget=forms.TextInput(attrs={'disabled': 'disabled', 'style': 'display: none;'}),
                           required=False, label=False)

    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }
