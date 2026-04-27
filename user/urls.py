from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('register',views.registeration,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name='logout'),
    path('email-verification/<str:uidb64>/<str:token>',views.email_verification,name="email_verification"),
    path('email-verification-send',views.email_verification_send,name="email_verification_send"),
    path('email-verification-send-failed',views.email_verification_send_failed,name="email_verification_send_failed"),
    path('profile',views.profile,name="profile"),
    path('password-reset',auth_view.PasswordResetView.as_view(template_name='user/password-reset.html'),name="password_reset"),
    path('password-reset-done',auth_view.PasswordResetDoneView.as_view(template_name='user/password-reset-done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='user/password-reset-confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name="user/password-reset-complete.html"),name="password_reset_complete"),
]