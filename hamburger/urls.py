"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name='hamburger'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('mac_list/', views.MacListView.as_view(), name='mac_list'),
    path('mos_list/', views.MosListView.as_view(), name='mos_list'),
    path('burgerking_list/', views.BurgerKingListView.as_view(), name='burgerKing_list'),
    path('mac_detail/<int:pk>/', views.MacDetailView.as_view(), name='mac_detail'),
    path('mos_detail/<int:pk>/', views.MosDetailView.as_view(), name='mos_detail'),
    path('burgerking_detail/<int:pk>/', views.BurgerKingDetailView.as_view(), name='burgerking_detail'),
]

