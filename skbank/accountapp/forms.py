from django import forms
from django.conf import Settings
from django.http import request

from .models import  Branch, Person

MATERIAL_CHOICES = (
    ('debitcard', 'Debit Card'),
    ('creditcard', 'Credit Card'),
    ('chequebook', 'Cheque Book'),)


class PersonForm(forms.ModelForm):
    materialrequired = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 choices=MATERIAL_CHOICES)

    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'age', 'gender','phone_number','email_id','address', 'account_type', 'district', 'branch', 'materialrequired')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
