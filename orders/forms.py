from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Иванов'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ivan_ivanov@example.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Россия, Москва, ул. Ленина, дом 10'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
