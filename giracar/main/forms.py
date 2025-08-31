from django import forms
from .models import CarRequest

class CarRequestForm(forms.ModelForm):
    class Meta:
        model = CarRequest
        fields = ['name', 'make', 'model', 'year', 'total_price', 'monthly_payment', 'details', 'contact']
        labels = {
            'name': 'Nome',
            'make': 'Marca do carro',
            'model': 'Modelo do carro',
            'year': 'Ano de fabricação',
            'total_price': 'Preço total (R$)',
            'monthly_payment': 'Quanto posso pagar por mês (R$)',
            'details': 'Detalhes adicionais',
            'contact': 'Contato (email ou telefone)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'make': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'model': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'year': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'total_price': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2 currency'}),
            'monthly_payment': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2 currency'}),
            'details': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'rows':4}),
            'contact': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
        }
