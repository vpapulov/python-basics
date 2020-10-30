from django.urls import path
from .views import index_view
from .views import money_income_list_view

app_name = 'koshelek'

urlpatterns = [
    path('', index_view, name='index'),
    path('income/', money_income_list_view, name='index'),
]