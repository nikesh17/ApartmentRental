from django import forms

from .models import Support

# class ComplaintForm(forms.ModelForm):
#     class Meta:
#         model = Complaint
#         fields = ('name','email','phone_number','apartment_id','message')
#         widgets ={
#             'name': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Name'}),
#             'email': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Email address'}),
#             'phone_number': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Phone number'}),
#             'apartment_id': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Apartment'}),
#             'message': forms.Textarea(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm','placeholder':'Write your message...'}),
#         }

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ('name','email','phone_number','apartment_id','message')
        widgets ={
            'name': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Name'}),
            'email': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Email address'}),
            'phone_number': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Phone number'}),
            'apartment_id': forms.TextInput(attrs={'class':'w-full rounded-lg border-gray-200 p-3 text-sm','placeholder':'Apartment'}),
            'message': forms.Textarea(attrs={'class': 'mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm','placeholder':'Write your message...'}),
        }        

