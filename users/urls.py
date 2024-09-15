from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('change-password/', views.UserChangePasswordView.as_view(), name='password_change'),
    path('change-password/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),

    path('profile/edit', views.ProfileEditView.as_view(), name='profile_edit'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),

    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')

]
