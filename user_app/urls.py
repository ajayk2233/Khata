from django.urls import path
from .views import signup,signin,signout,edit_profile
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordChangeDoneView,PasswordChangeView,PasswordResetCompleteView

urlpatterns = [
# User Related Operations
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('edit_profile/',edit_profile,name='edit_profile'),
    # Password Change links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    # Password Reset links
    path('password_reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]