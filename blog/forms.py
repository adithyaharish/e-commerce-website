from django import forms

class CheckoutForm(forms.Form):
    phone=forms.CharField(max_length=12)
    street_address = forms.CharField()
    appartment_address = forms.CharField(required=False)
    state = forms.CharField()
    zip = forms.CharField(required=False)