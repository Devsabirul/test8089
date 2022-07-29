from django import forms
from my_app.models import ProductDetails


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'})

        }
