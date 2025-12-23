from django import forms
from pipoca.models import Pipoca

class PipocaModelForm(forms.ModelForm):
    class Meta:
        model = Pipoca
        fields = '__all__'    
    #validação de preço do produto o valor deve ser acima de 2,00
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 2:
            self.add_error('preco', 'Valor para cadastro deve ser acima de R$2,00')
        else:
            return preco