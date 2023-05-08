from django import forms


class CreateArticle(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    body = forms.CharField()
    