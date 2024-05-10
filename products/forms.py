from django import forms
from.models import Contact,Part


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = Contact
        fields = '__all__'


class PartSearchForm(forms.ModelForm):
    name = forms.CharField(required=True,label='first_name')
    last_name = forms.CharField(required=True,label='last_name')
    phone = forms.CharField(required=True,label='contact_number')
    

    class Meta:
        model = Part
        fields = ['part_name','car_model']