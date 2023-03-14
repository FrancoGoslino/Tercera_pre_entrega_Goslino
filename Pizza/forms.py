from django import forms
from Pizza.models import Bebida, Pizza, Empanada

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = '__all__'

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        
class EmpanadaForm(forms.ModelForm):
    class Meta:
        model = Empanada
        fields = '__all__'