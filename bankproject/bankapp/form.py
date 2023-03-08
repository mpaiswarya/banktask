from django import forms

from bankapp.models import Person, Branch
Account_Type = [
    ('savings account', 'savings account'),
    ('current account', 'current account'),
]
Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

MATERIAL_CHOICES=[
    ('debit card', 'debit card'),
    ('credit card', 'credit card'),
    ('cheque book','cheque book')
]
class PersonCreationForm(forms.ModelForm):
    Accounttype=forms.CharField(max_length=30,widget=forms.Select(choices=Account_Type))
    Gender=forms.CharField(max_length=20,widget=forms.Select(choices=Gender))
    Materials=forms.CharField(label='What type Material using',widget=forms.RadioSelect(choices=MATERIAL_CHOICES))
    class Meta:
        model = Person
        fields = '__all__'
