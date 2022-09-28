from django.urls import path
from . import views
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    #Mac
    path('Mac-create/',views.MacCreateView.as_view(), name = "Mac_create"),
    path('Mac-update/<int:pk>/',views.MacUpdateView.as_view(),name = "Mac_update"),
    path('Mac-delete/<int:pk>/',views.MacDeleteView.as_view(),name = "Mac_delete"),
    #Mos
    path('Mos-create/',views.MosCreateView.as_view(), name = "Mos_create"),
    path('Mos-update/<int:pk>/',views.MosUpdateView.as_view(),name = "Mos_update"),
    path('Mos-delete/<int:pk>/',views.MosDeleteView.as_view(),name = "Mos_delete"),
    #BurgerKing
    path('BurgerKing-create/',views.BurgerKingCreateView.as_view(), name = "BurgerKing_create"),
    path('BurgerKing-update/<int:pk>/',views.BurgerKingUpdateView.as_view(),name = "BurgerKing_update"),
    path('BurgerKing-delete/<int:pk>/',views.BurgerKingDeleteView.as_view(),name = "BurgerKing_delete"),
]
