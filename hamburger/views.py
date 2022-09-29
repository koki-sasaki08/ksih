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
    paginate_by = 8

    def get_queryset(self):
        macs = Mac.objects.filter(user=self.request.user)
        return macs

class MosListView(generic.ListView):
    model = Mos
    template_name = 'Mos_list.html'
    paginate_by = 8

    def get_queryset(self):
        macs = Mos.objects.filter(user=self.request.user)
        return macs

class BurgerKingListView(generic.ListView):
    model = BurgerKing
    template_name = 'burgerKing_list.html'
    paginate_by = 8

    def get_queryset(self):
        macs = BurgerKing.objects.filter(user=self.request.user)
        return macs

class MacDetailView(generic.DetailView):
    model = Mac
    template_name = 'mac_detail.html'

class MosDetailView(generic.DetailView):
    model = Mos
    template_name = 'mos_detail.html'

class BurgerKingDetailView(generic.DetailView):
    model = BurgerKing
    template_name = 'burgerking_detail.html'