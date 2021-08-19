from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import DataView, HomeView, CustomerRegView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),
         name='login'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    # path('accounts/profile/', views.add_show, name='profile'),
    path('register', CustomerRegView.as_view(), name="register"),
    path('update/', views.update, name='update'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


]
