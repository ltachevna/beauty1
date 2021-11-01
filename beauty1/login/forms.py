from django import forms
# from django.core.validators import validate_email
import django

# class MultiEmailField(forms.Field):
#     def to_python(self, value):
#         if not value:
#             return []
#         return value.split(',')
#
#     def validate(self, value):
#         for email in value:
#             validate_email(email)

class Sing_inForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите ваш email",
        })
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите ваш пароль"
        })
    )


class RegisterForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите ваш email",
        })
    )

    password = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите ваш пароль"
        })
    )

    repeat_password = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Повторите ваш пароль"
        })
    )


class ContactForm(forms.Form):

    def clean_sing(self, email):
        email = self.email
        data = self.clean_data['sing']
        if self.email not in data:
            raise forms.ValidationError()
        return data

    def clean_register(self, email, password, repeat_password):
        email = self.email
        password = self.password
        repeat_password = self.repeat_password
        data = self.clean_data['register']
        if self.email not in data:
            if self.password != self.repeat_password:
                raise forms.ValidationError("Ваши пароли не совпадают")
            raise forms.ValidationError
        return data

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")
        if cc_myself and subject:
            if "help" not in subject:
                raise forms.ValidationError()






