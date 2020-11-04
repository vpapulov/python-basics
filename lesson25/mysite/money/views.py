from django.shortcuts import render
from .models import Account
from django.views.generic import ListView, DetailView


class AccountListView(ListView):
    model = Account
    template_name = 'accounts/list.html'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/detail.html'