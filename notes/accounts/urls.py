from django.urls import path
from accounts.views import LoginView, RegisterView, LogoutView, DashboardView
from accounts import views 

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('',DashboardView.as_view(),name='dashboard'),

]