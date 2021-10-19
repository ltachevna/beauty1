from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_lenght=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placehoder": "Ваше имя"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placehoder": "Оставьте комментарии"

        })
    )