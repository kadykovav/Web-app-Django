import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.core import validators


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(label='Телефон', min_length=10, max_length=12,
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.RegexValidator(regex=r'^\+?7?\d{10}$',
                                                                  message='Некорректный формат номера телефона',
                                                                  code='invalid_phone_number')])

    class Meta:
        model = get_user_model()
        this_year = datetime.date.today().year
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'photo', 'gender', 'date_birth']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'photo': 'Аватарка',
            'gender': 'Пол',
            'date_birth': 'Дата рождения'

        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': ''}),
            'date_birth': forms.SelectDateWidget(attrs={'class': 'form-select'},
                                                 years=tuple(range(this_year - 100, this_year)))
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', min_length=10, max_length=12,
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.RegexValidator(regex=r'^\+?7?\d{10}$',
                                                                  message='Некорректный формат номера телефона',
                                                                  code='invalid_phone_number')])

    class Meta:
        model = get_user_model()
        this_year = datetime.date.today().year
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'gender', 'date_birth', 'password1',
                  'password2', ]
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'gender': 'Пол',
            'date_birth': 'Дата рождения',
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': ''}),
            'date_birth': forms.SelectDateWidget(attrs={'class': 'form-select'},
                                                 years=tuple(range(this_year - 100, this_year)))
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        print(email)
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким E-mail уже существует')
        return email


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Повторите пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
