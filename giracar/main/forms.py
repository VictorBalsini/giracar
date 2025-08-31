from django import forms
from .models import CarRequest

class CarRequestForm(forms.ModelForm):
    class Meta:
        model = CarRequest
        fields = ['name', 'make', 'model', 'year', 'details', 'local', 'contact']
        labels = {
            'name': 'Nome',
            'make': 'Marca do carro',
            'model': 'Modelo do carro',
            'year': 'Ano de fabricação',
            'details': 'Detalhes adicionais',
            'local': 'Cidade onde procura',
            'contact': 'Contato (email ou telefone)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'make': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'model': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'year': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'details': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'rows': 4}),
            'local': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'contact': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if field == 'contact':
                continue 
            value = cleaned_data.get(field)
            if isinstance(value, str):  # Only format strings
                cleaned_data[field] = value.strip().capitalize()
        return cleaned_data
