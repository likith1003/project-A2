from django import forms
from seller.models import *
import re
class SellerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        help_texts = {'username': ''}

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        exclude = ['user', 'seller_id']
    
    def clean_contact(self):
        pno = self.cleaned_data.get('contact')
        if re.match('^(\+91|\+91\ |0)?[6-9]\d{9}$', pno):
            return pno
        return None


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['seller', 'pid']