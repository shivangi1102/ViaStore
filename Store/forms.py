from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order

class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=30, required=False, help_text='Optional.',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password1 = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                 widget=forms.TextInput(attrs={'placeholder': 'First_name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
                                widget=forms.TextInput(attrs={'placeholder': 'Last_name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )





PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)





class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']