from django.urls import path
from register import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'register'

urlpatterns = [
  #path('profile/', views.profile, name='profile'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='login.html'), name='logout'),
  #path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html', success_url='/profile/'), name='password_change'),
  path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]