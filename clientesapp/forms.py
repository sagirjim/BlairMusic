from django import forms
from clientesapp.models import Cliente, Orden


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ordenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'



