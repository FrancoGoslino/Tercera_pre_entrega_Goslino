from django import forms
from Pizza.models import Bebida

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = '__all__'