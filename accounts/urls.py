from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    # path('logout/', LogoutView.as_view(nex_page='home'), name='logout'),
    path('logout/', views.logout_view, name='logout'),
]
