from django.contrib import admin
from django.urls import path, include
app_name = "common"

from admin.common.views import DashboardView, deposit, deposit_pending, deposit_complete, withdraw, withdraw_complete, withdraw_pending, deposit_status, withdraw_status, add_user, delete_user, feedback, request_user, request_pending, request_complete, complete_user

from django.contrib.auth import views as auth_views

urlpatterns = [    
    path('', DashboardView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('request/user', request_user, name='request-user'),
    path('request/pending', request_pending, name="requestPending"),
    path('request/complete', request_complete, name="requestComplete"),

    path('complete/user', complete_user, name="completeUser"),

    path('deposit', deposit, name="adminDeposit"),
    path('deposit/pending', deposit_pending, name="depositPending"),
    path('deposit/complete', deposit_complete, name="depositComplete"),

    path('feedback', feedback, name="adminFeedback"),

    path('withdraw', withdraw, name="adminWithdraw"),
    path('withdraw/pending', withdraw_pending, name="withdrawPending"),
    path('withdraw/complete', withdraw_complete, name="withdrawComplete"),

    path('deposit/status', deposit_status, name="depositStatus"),
    path('withdraw/status', withdraw_status, name="withdrawStatus"),

    path('add/user', add_user, name='add-user'),
    path('delete/user', delete_user, name="deleteUser"),

    path('login/', auth_views.LoginView.as_view(
    template_name='common/login.html'
    ),
    name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
        ),
        name='logout'
    ),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

