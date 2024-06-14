from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.regiister,name="register"),
    path('home/',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name='ft_app1/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='ft_app1/logout.html'), name='logout'),
    path('bar/',views.bar,name="navbar"),
    path('addinc/',views.addinc,name="addinc"),
    path('addrem/',views.addrem,name="addrem"),
    path('addexp/',views.addexp,name="addexp"),
    path('uprof/',views.uprof,name="uprof"),
    path('viewinc/',views.viewinc,name="viewinc"),
    path('viewexp/',views.viewexp,name="viewexp"),
    path('viewrem/',views.viewrem,name="viewrem"),
    path('link/',views.link,name="link"),
    path('linkview/',views.linkview,name="linkview"),
]