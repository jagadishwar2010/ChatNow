from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_user, name='login')
]
