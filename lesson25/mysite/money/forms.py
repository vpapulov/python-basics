from .models import Account
from django import forms


class AccountForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('name',)
        # fields = '__all__'
        # exclude = ('user',)
