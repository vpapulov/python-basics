from django.shortcuts import render
from .models import Account, MoneyIncome


def index_view(request):
    accounts = Account.objects.all()
    return render(request, 'koshelek/index.html', {'accounts': accounts})

def money_income_list_view(request):
    docs = MoneyIncome.objects.all()
    return render(request, 'koshelek/money_income_list.html', {'docs': docs})
