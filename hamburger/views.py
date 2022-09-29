from tokenize import Hexnumber
from django.shortcuts import render
from django.views import generic
from .models import Mac, Mos, BurgerKing, Favorite

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class MacListView(generic.ListView):
    model = Mac
    template_name = 'mac_list.html'

class MosListView(generic.ListView):
    model = Mos
    template_name = 'Mos_list.html'

class BurgerKingListView(generic.ListView):
    model = BurgerKing
    template_name = 'burgerKing_list.html'

class MacDetailView(generic.DetailView):
    model = Mac
    template_name = 'detail.html'

class MosDetailView(generic.DetailView):
    model = Mos
    template_name = 'detail.html'

class BurgerKingDetailView(generic.DetailView):
    model = BurgerKing
    template_name = 'detail.html'