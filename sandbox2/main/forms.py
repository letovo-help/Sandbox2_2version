from .models import Requests
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, ModelMultipleChoiceField
from .models import Category


class RequestsForm(ModelForm):
    class Meta:
        model = Requests
        #categories = ModelMultipleChoiceField(queryset=Category.objects.all())
        fields = ['title', 'additional_req', 'how_to_connect', 'description', 'is_anonimous']
        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название"
            }),
            "additional_req": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Дополнительные требования"
            }),

            "how_to_connect": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Как связаться"
            }),
            "description": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Описание",
                'id': 'description_of_req'
            }),
            "is_anonimous": CheckboxInput(attrs={
                'class': "form-control",
                'id': 'myonoffswitch'
            })
        }
