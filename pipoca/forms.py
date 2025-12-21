from django import forms
from pipoca.models import Pipoca

class PipocaModelForm(forms.ModelForm):
    class Meta:
        model = Pipoca
        fields = '__all__'    

