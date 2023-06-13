from django import forms
from .models import Apartment

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ('apartment_id', 'location', 'price', 'description','image')
        widgets = {
            'apartment_id': forms.TextInput(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'}),
            'location': forms.TextInput(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'}),
            'price': forms.TextInput(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'}),
            'description': forms.Textarea(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'}),
            'image': forms.ClearableFileInput(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm'}),
        }


class ApartmentEditForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = (
            "location",
            "price",
            "description",
            "image",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "appearance-none block w-full py-2 px-3 leading-tight border border-gray-300 rounded focus:outline-none focus:bg-white focus:border-gray-500"
                }
            )

