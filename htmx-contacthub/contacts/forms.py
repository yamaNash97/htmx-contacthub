from django import forms
from .models import Contact


class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= (
            'name', 'email'
        )    
        
    name= forms.CharField(
        widget= forms.TextInput(attrs={
            'class': 'input input-boarder w-full',
            'placeholder': 'Contact name'
        })
    )
    email= forms.EmailField(
         widget= forms.EmailInput(attrs={
            'class': 'input input-boarder w-full',
            'placeholder': 'Email Address'
        })
    )
