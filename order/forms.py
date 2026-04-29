from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    phone = forms.CharField(error_messages={'required':'please enter your phone number'})
    class Meta:
        model = Address
        exclude = ('user',)
        error_messages = {
            'full_name':{'required':'please enter your full name'},
            'line1':{'required':'please enter your line1 address'},
            'line2':{'required':'please enter your line2 address'},
            'city':{'required':'please enter your city'},
            'state':{'required':'please enter your state'},
            'country':{'required':'please enter your country'}
        }
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError('please enter digits only')
        if len(phone) != 10:
            raise forms.ValidationError('phone number must be 10 digits')
        return phone