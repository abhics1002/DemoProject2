from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django import forms
from person.models import Person, PhoneNumber

LABEL_CHOICES = (
    ("home", "home"),
    ("mobile", "mobile"),
    ("work", "work"),
    ("fax", "fax")
)

class PersonForm(ModelForm):
    title = forms.CharField(max_length=200)
    email = forms.EmailField()
    # class Meta:
    #     model = Person
    #     fields = '__all__'


class PhoneNumberForm(forms.Form):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'label']
    number = forms.CharField()
    label = forms.ChoiceField(choices=LABEL_CHOICES)


PhoneNumberFormSet = inlineformset_factory(Person, PhoneNumber,fields='__all__', fk_name='person', extra=2)
#PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=2)