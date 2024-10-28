from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='index'),
    path('fixture/<int:fixture_id>/', views.fixture_detail, name='fixture_detail'),
    path('teams/', views.team_list, name='team_list'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
      path('add_sport/', views.add_sport, name='add_sport'),
    path('add_team/', views.add_team, name='add_team'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('add_fixture/', views.add_fixture, name='add_fixture'),
    path('add_player/', views.add_player, name='add_player'),
]
