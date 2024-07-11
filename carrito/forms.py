from django import forms
from .models import ItemCarrito

class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad']
