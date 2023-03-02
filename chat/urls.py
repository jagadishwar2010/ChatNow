from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
