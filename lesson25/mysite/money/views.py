from .models import Account
from .forms import AccountForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin


class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class AccountListView(ListView):
    model = Account
    template_name = 'accounts/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['my_var'] = '123'
        return context


class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/detail.html'


class AccountCreateView(StaffOnlyMixin, CreateView):
    model = Account
    template_name = 'accounts/edit.html'
    success_url = '/accounts/'
    form_class = AccountForm
