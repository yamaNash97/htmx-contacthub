from django import forms
from .models import Contact
from django.core.exceptions import ValidationError


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
    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(user= self.initial.get('user'),email=email).exists():
            raise ValidationError("You already have a contact with this email address")
        return email