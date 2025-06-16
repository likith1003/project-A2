from django import forms
from customer.models import *
gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
]
class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        help_texts = {'username':''}

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ['user', 'customer_id']
    gender = forms.CharField(max_length=25, required=False, widget=forms.RadioSelect(choices=gender))