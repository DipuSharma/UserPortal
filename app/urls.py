from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import DataView, HomeView, CustomerRegView

urlpatterns = [

    re_path(r'', HomeView.as_view(), name="home"),
    re_path(r'accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                             authentication_form=LoginForm), name='login'),
    re_path(r'accounts/profile/', views.add_show, name='profile'),
    re_path(r'register', CustomerRegView.as_view(), name="register"),
    re_path(r'delete/<int:id>', views.delete, name="deleted"),
    re_path(r'<int:id>', views.update_data, name="update"),
    re_path(r'logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]
