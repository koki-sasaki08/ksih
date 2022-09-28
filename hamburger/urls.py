from django.urls import path
from . import views
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    #詳細
    path('hamburger-list/',views.HamburgerListView.as_view(),name = "hamburger_list"),
    path('hamburger-detail/<int:pk>/',views.HamburgerDetailView.as_view(),name = "hamburger_detail"),
    path('hamburger-create/',views.HamburgerCreateView.as_view(), name = "hamburger_create"),
    path('hamburger-update/<int:pk>/',views.HamburgerUpdateView.as_view(),name = "hamburger_update"),
    path('hamburger-delete/<int:pk>/',views.HamburgerDeleteView.as_view(),name = "hamburger_delete"),
    
]
