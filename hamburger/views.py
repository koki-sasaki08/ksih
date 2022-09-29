from tokenize import Hexnumber
from django.shortcuts import render
from django.views import generic
from .models import Mac, Mos, BurgerKing, Favorite

import logging

from django.urls import reverse_lazy
from django.contrib import messages

#作成
from .forms import MacCreateForm
from .forms import MosCreateForm
from .forms import BurgerKingCreateForm

#表示
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mac
from .models import Mos
from .models import BurgerKing

# Create your views here.
class IndexView(generic.TemplateView):
    template_name="index.html"

#mac
class MacCreateView(LoginRequiredMixin,generic.CreateView):
    model = Mac
    template_name = 'Mac_create.html'
    form_class = MacCreateForm
    success_url = reverse_lazy('hamburger:mac_list')

    def form_valid(self, form):
        hamburger = form.save(commit=False)
        hamburger.user = self.request.user
        hamburger.save()
        messages.success(self.request,'データを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"データの作成に失敗しました。")
        return super().form_invalid(form)

class MacUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Mac
    template_name = 'Mac_update.html'
    form_class = MacCreateForm

    def get_success_url(self):
        return reverse_lazy('hamburger:mac_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'データを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "データの更新に失敗しました。")
        return super().form_invalid(form)

class MacDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Mac
    template_name = 'Mac_delete.html'
    success_url = reverse_lazy('hamburger:mac_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "データを削除しました。")
        return super().delete(request, *args, **kwargs)





#Mos
class MosCreateView(LoginRequiredMixin,generic.CreateView):
    model = Mos
    template_name = 'Mos_create.html'
    form_class = MosCreateForm
    success_url = reverse_lazy('hamburger:mos_list')

    def form_valid(self, form):
        hamburger = form.save(commit=False)
        hamburger.user = self.request.user
        hamburger.save()
        messages.success(self.request,'データを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"データの作成に失敗しました。")
        return super().form_invalid(form)

class MosUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Mos
    template_name = 'Mos_update.html'
    form_class = MosCreateForm

    def get_success_url(self):
        return reverse_lazy('hamburger:mos_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'データを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "データの更新に失敗しました。")
        return super().form_invalid(form)

class MosDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Mos
    template_name = 'Mos_delete.html'
    success_url = reverse_lazy('hamburger:mos_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "データを削除しました。")
        return super().delete(request, *args, **kwargs)





#BurgerKing
class BurgerKingCreateView(LoginRequiredMixin,generic.CreateView):
    model = BurgerKing
    template_name = 'BurgerKing_create.html'
    form_class = BurgerKingCreateForm
    success_url = reverse_lazy('hamburger:burgerKing_list')

    def form_valid(self, form):
        hamburger = form.save(commit=False)
        hamburger.user = self.request.user
        hamburger.save()
        messages.success(self.request,'データを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"データの作成に失敗しました。")
        return super().form_invalid(form)

class BurgerKingUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = BurgerKing
    template_name = 'BurgerKing_update.html'
    form_class = BurgerKingCreateForm

    def get_success_url(self):
        return reverse_lazy('hamburger:burgerKing_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'データを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "データの更新に失敗しました。")
        return super().form_invalid(form)

class BurgerKingDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = BurgerKing
    template_name = 'BurgerKing_delete.html'
    success_url = reverse_lazy('hamburger:burgerKing_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "データを削除しました。")
        return super().delete(request, *args, **kwargs)


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