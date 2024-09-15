from django.contrib.auth import authenticate, login, logout, get_user_model, views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView

from .forms import LoginUserForm, RegistrationUserForm, ProfileUserForm, UserChangePasswordForm, UserResetPasswordForm


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('blog')


class UserChangePasswordView(PasswordChangeView):
    form_class = UserChangePasswordForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_edit.html'
    extra_context = {'title': 'Редактирование'}
    model = get_user_model()
    form_class = ProfileUserForm

    # success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile')


class ProfileDetailView(LoginRequiredMixin, DetailView, UpdateView):
    model = get_user_model()
    template_name = 'users/profile_detail.html'
    extra_context = {'title': 'Профиль'}
    context_object_name = 'user'
    form_class = ProfileUserForm

    def get_object(self, queryset=None):
        return self.request.user


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


class UserPasswordResetView(PasswordResetView):
    form_class = UserResetPasswordForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/password_reset_email.html'

