from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard/<order>/',views.dashboard, name='dashboard'),
    path('add_todo/',views.add_todo, name='add_todo'),
    path('delete_todo/<int:id>',views.delete_todo, name='delete_todo'),
    path('change_status/<int:id>/<str:status>',views.change_status, name='change_status'),
    path('pricing/', views.pricing, name='pricing' )
]
