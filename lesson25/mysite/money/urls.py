from django.urls import path
from .views import AccountListView, AccountDetailView

app_name = 'money'

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
]
