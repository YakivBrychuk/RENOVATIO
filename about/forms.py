from django import forms
from .models import CollaborateRequest

# A form for users to submit collaboration requests
class CollaborateForm(forms.ModelForm):
    class Meta:
        # Specify the model the form is based on
        model = CollaborateRequest  
        # Define which fields will be included in the form
        fields = ('name', 'email', 'message')  
