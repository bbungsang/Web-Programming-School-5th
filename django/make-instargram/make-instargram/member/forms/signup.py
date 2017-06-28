from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '아이디를 입력해주세요.'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력해주세요.'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 다시 입력해주세요.'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist!'
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Passwords mismatch!'
            )
        return password2

    def create_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password2']
        return User.objects.create_user(
            username=username,
            password=password,
        )