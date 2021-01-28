"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from users import views as users_views
from users.forms import CustomAuthForm

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('activate/<uidb64>/<token>/', users_views.activate, name='activate'),
                  path('', include('delivery.urls')),
                  path('password_reset/',
                       auth_views.PasswordResetView.as_view(template_name="users/password_reset_form.html"),
                       name='password_reset'),
                  path('password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
                       name='password_reset_done'),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                      auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
                      name='password_reset_confirm'),
                  path('reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
                       name='password_reset_complete'),
                  path('login/', auth_views.LoginView.as_view(template_name="users/login.html",authentication_form=CustomAuthForm), name="login"),
                  path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
                  path('register/', users_views.register, name="register"),
                  path('profile/', users_views.profile, name="profile"),
                  url('^', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
