from django import forms
from .models import Category, News


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150)
#     content = forms.CharField()
#     is_published = forms.BooleanField()
#     category = forms.ModelChoiceField(queryset=Category.objects.all())


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150,
#                             label='Название',
#                             widget=forms.TextInput(attrs={'class':'form-control'}))
#     content = forms.CharField(label='текст',
#                               required=False,
#                               widget=forms.Textarea(attrs={'class':'form-control', 'rows':7}))
#     is_published = forms.BooleanField(label='Опубликовано',
#                                       initial=True,
#                                       widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория',
#                                       empty_label=None,
#                                       widget=forms.Select(attrs={'class':'form-select'}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':7}),
            'is_published': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'category': forms.Select(attrs={'class':'form-select'})
        }