from django.urls import path
from .views import AccountListView, AccountDetailView, AccountCreateView

app_name = 'accounts'

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('accounts/create/', AccountCreateView.as_view(), name='account-create'),
]
