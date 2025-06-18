from django import forms
from .models import LostItem

class newFoundForm(forms.ModelForm):

    class Meta:
        model = LostItem
        fields = ['item_name', 'item_picture', 'item_description', 'contactEmail', 'found_at', 'found_datetime']

        widgets = {
            'item_name' : forms.TextInput(attrs={'class':'form-control'}),
            'item_description' : forms.Textarea(attrs={'class':'form-control'}),
            'found_datetime' : forms.DateTimeInput(attrs={'class':'form-control', 'type' : 'datetime-local'}),
            'contactEmail' : forms.EmailInput(attrs={'class':'form-control'}),
            'found_at' : forms.TextInput(attrs={'class':'form-control'}),
            'item_picture' : forms.FileInput(attrs={'class':'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        picture = cleaned_data.get("item_picture")
        if picture:
            if picture.size > 5*1024*1024: #5mb
                  self.add_error('item_picture', "Image file too large (max 5MB)")
        return cleaned_data