from tokenize import Hexnumber
from django.shortcuts import render
from django.views import generic

import logging

from django.urls import reverse_lazy
from django.contrib import messages

#作成
from .forms import HamburgerCreateForm

#表示                                                       #アクセス制御
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

from .models import Hamburger

#アクセス制御
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

#アクセス制御
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        hamburger = get_object_or_404(Hamburger, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == hamburger.user


# Create your views here.
class IndexView(generic.TemplateView):
    template_name="index.html"


class HamburgerListView(LoginRequiredMixin,generic.ListView):
    model = Hamburger
    template_name = 'hamburger_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Hamburger.objects.filter(user = self.request.user).order_by('-created_at')
        return diaries

class HamburgerDetailView(LoginRequiredMixin,OnlyYouMixin,generic.DeleteView):
    model = Hamburger
    template_name = 'hamburger_detail.html'



class HamburgerCreateView(LoginRequiredMixin,generic.CreateView):
    model = Hamburger
    template_name = 'hamburger_create.html'
    form_class = HamburgerCreateForm
    success_url = reverse_lazy('hamburger:hamburger_list')

    def form_valid(self, form):
        hamburger = form.save(commit=False)
        hamburger.user = self.request.user
        hamburger.save()
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"日記の作成に失敗しました。")
        return super().form_invalid(form)

class HamburgerUpdateView(LoginRequiredMixin,OnlyYouMixin,generic.UpdateView):
    model = Hamburger
    template_name = 'hamburger_update.html'
    form_class = HamburgerCreateForm

    def get_success_url(self):
        return reverse_lazy('hamburger:hamburger_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

class HamburgerDeleteView(LoginRequiredMixin,OnlyYouMixin,generic.DeleteView):
    model = Hamburger
    template_name = 'hamburger_delete.html'
    success_url = reverse_lazy('hamburger:hamburger_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)