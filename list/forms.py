from django import forms
from .models import MyList

class AddItemForm(forms.ModelForm):
    class Meta:
        model = MyList
        fields = '__all__'
        widgets = {
            'customer':forms.TextInput(attrs={'class': 'form-control','value':'','id':'username','type':'hidden'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
        }