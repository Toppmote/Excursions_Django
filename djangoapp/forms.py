from .models import *
from django.forms import *


class ExcursionForm(ModelForm):
    class Meta:
        model = Excursion
        guide = ModelChoiceField(queryset=Guide.objects.all(), initial=0)
        city = ModelChoiceField(queryset=City.objects.all(), initial=0)
        fields = ["name", "description", "date", "guide", "city"]
        widgets = {
            "name": TextInput(attrs={
                'id': "floatingName",
                'class': "form-control rounded-4",
                'placeholder': "Name",
                'maxLength': 100
            }),
            "description": Textarea(attrs={
                'id': "floatingDesc",
                'class': "form-control rounded-4",
                'placeholder': "desc",
                'rows': 10,
                'maxLength': 1000
            }),
            "date": DateInput(attrs={
                'id': "floatingDate",
                'class': "form-control rounded-4",
                'placeholder': "2000-06-02",
                'type': 'date'
            })
        }
